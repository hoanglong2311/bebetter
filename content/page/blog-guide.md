---
title: "Blog Guide"
date: 2024-03-31
description: "Comprehensive guide for managing and writing content for this blog"
type: "page"
url: "/blog-guide"
---

## Blog Guide

# Blog Management Guide

This guide will help you understand how to manage and write content for this blog. Whether you're creating new posts, configuring the site, or troubleshooting issues, you'll find the information you need here.

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

## Creating New Posts

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

## Writing Tips

### Content Organization
- Use clear headings (##, ###)
- Include code blocks with syntax highlighting
- Add relevant images
- Keep paragraphs short
- Use lists for better readability

### Markdown Formatting
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

### Adding Images and Links
```markdown
[Link text](https://example.com)
![Image alt text](img/image.jpg)
```

### Creating Tables
```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
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

### 3. Draft Management
- Use `draft: true` for unpublished posts
- Preview with `hugo server -D`
- Set to `false` when ready to publish

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
