#!/usr/bin/env python3
import os
import re
import shutil
import yaml
from datetime import datetime, timedelta
import random

# Configuration
KNOWLEDGE_BASE_DIR = "knowledge_base"
HUGO_CONTENT_DIR = "content"
CATEGORIES_MAP = {
    "00-Maps of Content (MOCs)": "Maps of Content",
    "10-Core Concepts": "Core Concepts", 
    "20-Technologies": "Technologies",
    "30-Repositories": "Repositories",
    "40-Projects": "Projects",
    "50-Interview Prep": "Interview Prep",
    "60-Cheat Sheets": "Cheat Sheets",
    "70-Daily Journal": "Daily Journal"
}

# Create necessary directories
for category in CATEGORIES_MAP.values():
    os.makedirs(f"{HUGO_CONTENT_DIR}/categories/{category.lower().replace(' ', '-')}", exist_ok=True)

def sanitize_filename(filename):
    """Convert filename to URL-friendly slug"""
    # Remove file extension
    filename = os.path.splitext(filename)[0]
    
    # Remove any numbering prefix like 101a-, 102-
    filename = re.sub(r'^\d+[a-z]?-?', '', filename)
    
    # Replace spaces and special chars with hyphens
    filename = re.sub(r'[^a-zA-Z0-9]', '-', filename)
    
    # Convert to lowercase and remove consecutive hyphens
    filename = re.sub(r'-+', '-', filename.lower())
    
    # Remove leading/trailing hyphens
    filename = filename.strip('-')
    
    return filename

def extract_title(content):
    """Extract the title from markdown content"""
    # Try to find a heading
    heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if heading_match:
        return heading_match.group(1)
    
    # If no heading, use the first non-empty line
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            return line.strip()
    
    return "Untitled"

def get_tags_from_path(file_path):
    """Generate tags based on file path and content"""
    tags = []
    
    # Add parent directory name as a tag
    parent_dir = os.path.basename(os.path.dirname(file_path))
    if parent_dir and not parent_dir.startswith(tuple(CATEGORIES_MAP.keys())):
        # Clean up tag
        tag = re.sub(r'^\d+[a-z]?-?', '', parent_dir)
        tag = re.sub(r'[^a-zA-Z0-9\s]', '', tag)
        if tag:
            tags.append(tag)
    
    return tags

def generate_date(file_path):
    """Generate a date for the post, prioritizing dates in filenames"""
    # Check if filename has a date format like 2023-10-01
    filename = os.path.basename(file_path)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if date_match:
        return date_match.group(1)
    
    # If no date in filename, use a date from the last 6 months
    today = datetime.now()
    random_days = random.randint(1, 180)  # Random date in the last 6 months
    random_date = today - timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def convert_internal_links(content, file_map):
    """Convert internal links to Hugo-style permalinks"""
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Skip external links
        if link_path.startswith(('http://', 'https://')):
            return match.group(0)
        
        # Remove file extension and anchors
        clean_path = link_path.split('#')[0]
        if clean_path.endswith('.md'):
            clean_path = clean_path[:-3]
        
        # Normalize path
        normalized_path = os.path.normpath(clean_path)
        
        # Check if we have this file in our map
        if normalized_path in file_map:
            hugo_link = file_map[normalized_path]
            if '#' in link_path:
                # Preserve anchors
                anchor = link_path.split('#', 1)[1]
                hugo_link = f"{hugo_link}#{anchor}"
            return f"[{link_text}]({hugo_link})"
        
        # Return original if not found
        return match.group(0)
    
    # Replace markdown links
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)

def create_hugo_post(source_path, category, file_map):
    """Convert a knowledge base markdown file to a Hugo post"""
    # Read the source file
    with open(source_path, 'r') as f:
        content = f.read()
    
    # Extract title from content
    title = extract_title(content)
    
    # Generate filename
    filename = sanitize_filename(os.path.basename(source_path))
    
    # Generate tags and date
    tags = get_tags_from_path(source_path)
    date = generate_date(source_path)
    
    # Create frontmatter
    frontmatter = {
        'title': title,
        'date': date,
        'draft': False,
        'categories': [category],
        'tags': tags
    }
    
    # Convert content to Hugo-style
    converted_content = convert_internal_links(content, file_map)
    
    # Check if content already has frontmatter (starts with ---)
    if not converted_content.startswith('---'):
        # Add frontmatter if it doesn't exist
        frontmatter_str = '---\n' + yaml.dump(frontmatter) + '---\n\n'
        converted_content = frontmatter_str + converted_content
    
    # Write to Hugo content directory
    hugo_posts_dir = os.path.join(HUGO_CONTENT_DIR, 'post')
    os.makedirs(hugo_posts_dir, exist_ok=True)
    
    # Create post file
    post_path = os.path.join(hugo_posts_dir, f"{filename}.md")
    with open(post_path, 'w') as f:
        f.write(converted_content)
    
    return f"/post/{filename}/"

def process_knowledge_base():
    """Process all files in the knowledge base"""
    file_map = {}  # Maps original file paths to Hugo URLs
    
    # First pass: build the file map
    for category_dir, hugo_category in CATEGORIES_MAP.items():
        kb_category_path = os.path.join(KNOWLEDGE_BASE_DIR, category_dir)
        if not os.path.exists(kb_category_path):
            continue
        
        # Walk through all files in this category
        for root, _, files in os.walk(kb_category_path):
            for file in files:
                if not file.endswith('.md'):
                    continue
                
                source_path = os.path.join(root, file)
                rel_path = os.path.relpath(source_path, KNOWLEDGE_BASE_DIR)
                
                # Store normalized path for link conversion
                normalized_path = os.path.normpath(rel_path)
                filename = sanitize_filename(file)
                
                file_map[normalized_path] = f"/post/{filename}/"
    
    # Second pass: convert files to Hugo posts
    for category_dir, hugo_category in CATEGORIES_MAP.items():
        kb_category_path = os.path.join(KNOWLEDGE_BASE_DIR, category_dir)
        if not os.path.exists(kb_category_path):
            continue
        
        # Create category index file if it doesn't exist
        category_slug = hugo_category.lower().replace(' ', '-')
        category_index = os.path.join(HUGO_CONTENT_DIR, 'categories', category_slug, '_index.md')
        
        if not os.path.exists(category_index):
            with open(category_index, 'w') as f:
                f.write(f"""---
title: "{hugo_category}"
description: "Content related to {hugo_category.lower()}"
slug: "{category_slug}"
style:
    background: "#2a9d8f"
    color: "#fff"
---

{hugo_category} contains content related to {hugo_category.lower()}.
""")
        
        # Walk through all files in this category
        for root, _, files in os.walk(kb_category_path):
            for file in files:
                if not file.endswith('.md'):
                    continue
                
                source_path = os.path.join(root, file)
                create_hugo_post(source_path, hugo_category, file_map)
    
    print(f"Knowledge base import complete! Files were converted to Hugo posts in {HUGO_CONTENT_DIR}/post/")

if __name__ == "__main__":
    process_knowledge_base() 