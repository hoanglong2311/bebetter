import os
import glob
import yaml
import random
import re

# --- Configuration ---
POST_DIR = "content/post"
IMAGE_BASE_URL = "https://source.unsplash.com/random/1600x900"
# --- End Configuration ---

def update_post_images():
    """
    Finds all markdown files in POST_DIR, parses their front matter,
    updates the 'image' field with a random Unsplash URL, and saves the changes.
    """
    print(f"Searching for markdown files in '{POST_DIR}'...")
    md_files = glob.glob(os.path.join(POST_DIR, "*.md"))

    if not md_files:
        print("No markdown files found.")
        return

    print(f"Found {len(md_files)} markdown files. Processing...")
    processed_count = 0
    error_count = 0

    # Regex to split front matter from content
    front_matter_pattern = re.compile(r'^---\s*$(.*?)^---\s*$(.*)', re.MULTILINE | re.DOTALL)

    for filepath in md_files:
        filename = os.path.basename(filepath)
        print(f"Processing '{filename}'...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            match = front_matter_pattern.match(content)
            if not match:
                print(f"  Skipping '{filename}': Could not find YAML front matter.")
                continue

            front_matter_str = match.group(1)
            body_content = match.group(2)

            try:
                data = yaml.safe_load(front_matter_str)
                if data is None: # Handle empty front matter
                    data = {}
            except yaml.YAMLError as e:
                print(f"  Skipping '{filename}': Error parsing YAML front matter: {e}")
                error_count += 1
                continue

            # Generate unique cache-busting parameter for the image URL
            cache_bust = random.randint(10000, 99999)
            new_image_url = f"{IMAGE_BASE_URL}?cachebust={cache_bust}"
            data['image'] = new_image_url

            # Dump updated front matter back to string, ensuring proper format
            updated_front_matter_str = yaml.dump(data, default_flow_style=False, allow_unicode=True)

            # Reconstruct the file content
            updated_content = f"---\n{updated_front_matter_str}---\n{body_content}"

            # Write the updated content back to the file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"  Updated image for '{filename}' to: {new_image_url}")
            processed_count += 1

        except Exception as e:
            print(f"  Error processing '{filename}': {e}")
            error_count += 1

    print("\n--- Summary ---")
    print(f"Successfully processed: {processed_count}")
    print(f"Skipped/Errors:       {error_count}")
    print("----------------")

if __name__ == "__main__":
    # Check for PyYAML dependency
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML library not found.")
        print("Please install it using: pip install PyYAML")
        exit(1)

    update_post_images()
