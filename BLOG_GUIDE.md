# Hugo Blog Management Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Post Creation](#post-creation)
3. [Configuration](#configuration)
4. [Directory Structure](#directory-structure)
5. [Best Practices](#best-practices)
6. [Useful Commands](#useful-commands)

## Quick Start

### Initial Setup
1. Make sure Hugo is installed
2. Clone the theme: `themes/hugo-theme-stack`
3. Create basic structure:
   ```bash
   mkdir -p content/{post,page,categories} static/img
   ```

### Running the Blog
- Preview locally: `hugo server -D`
- Build for production: `hugo`
- Clean build cache: `hugo --gc`

## Post Creation

### Method 1: Using Hugo Command (Recommended)
```bash
hugo new post/your-post-title.md
```

### Method 2: Manual Creation
1. Create a new `.md` file in `content/post/`
2. Use this template:

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
lastmod: YYYY-MM-DD  # Optional
image: img/your-image.jpg
categories:
  - Category1
  - Category2
tags:
  - Tag1
  - Tag2
draft: false  # Set to true for unpublished posts
description: "Brief description"  # Optional
---

Your content here...
```

## Configuration

### Main Configuration (config.yaml)
```yaml
baseURL: "https://your-domain.com/"
languageCode: "en-us"
title: "Your Blog Title"
theme: hugo-theme-stack

params:
  profileMode:
    enabled: true
    title: "Your Name"
    subtitle: "Your Tagline"
    imageUrl: "img/avatar.png"
    buttons:
      - name: Posts
        url: posts
      - name: About
        url: about

  socialIcons:
    - name: github
      url: "https://github.com/yourusername"
    - name: linkedin
      url: "https://linkedin.com/in/yourusername"
```

## Directory Structure
```
your-blog/
├── content/
│   ├── post/           # Blog posts
│   └── page/           # Static pages
├── static/
│   └── img/           # Images
├── config.yaml        # Main configuration
└── themes/
    └── hugo-theme-stack/
```

## Best Practices

### 1. Images
- Place in `static/img/`
- Use descriptive filenames
- Optimize before adding
- Recommended formats: JPG, PNG, WebP

### 2. Categories and Tags
- Categories: Keep broad (e.g., Technology, Life, Learning)
- Tags: Use for specific topics
- Be consistent with naming

### 3. Content Organization
- Use clear headings (##, ###)
- Include code blocks with syntax highlighting
- Add relevant images
- Keep paragraphs short
- Use lists for better readability

### 4. Draft Management
- Use `draft: true` for unpublished posts
- Preview with `hugo server -D`
- Set to `false` when ready to publish

## Useful Commands

```bash
# Create new post
hugo new post/your-post.md

# Preview site with drafts
hugo server -D

# Build site
hugo

# Clean build cache
hugo --gc

# Show help
hugo --help
```

## Markdown Tips

### Basic Formatting
```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
1. Numbered list

> Blockquote

`Inline code`

```language
Code block
```

### Links and Images
```markdown
[Link text](https://example.com)
![Image alt text](img/image.jpg)
```

### Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

## Troubleshooting

### Common Issues
1. **Images not showing**
   - Check path in front matter
   - Ensure image is in `static/img/`
   - Verify file extension

2. **Changes not visible**
   - Clear browser cache
   - Restart Hugo server
   - Check for typos in front matter

3. **Build errors**
   - Check YAML syntax
   - Verify file paths
   - Ensure theme is properly installed

## Resources
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Stack Theme Documentation](https://stack.jimmycai.com/)
- [Markdown Guide](https://www.markdownguide.org/)