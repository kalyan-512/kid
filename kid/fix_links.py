#!/usr/bin/env python3
"""Fix all .html extensions in internal links to use clean URLs"""

import re
from pathlib import Path

# List of all HTML files
html_files = [
    'index.html', 'about.html', 'programs.html', 'contact.html',
    'admission.html', 'blog.html', 'franchise.html', 'preschools.html',
    'privacy-policy.html', 'terms-conditions.html',
    'preschool-gachibowli.html', 'preschool-nallagandla.html',
    'preschool-attapur.html', 'preschool-begumpet.html', 'preschool-ameerpet.html'
]

# Mapping of .html links to clean URLs
replacements = {
    r'href="index\.html"': 'href="/"',
    r'href="about\.html"': 'href="/about"',
    r'href="programs\.html"': 'href="/programs"',
    r'href="contact\.html"': 'href="/contact"',
    r'href="admission\.html"': 'href="/admission"',
    r'href="blog\.html"': 'href="/blog"',
    r'href="franchise\.html"': 'href="/franchise"',
    r'href="preschools\.html"': 'href="/preschools"',
    r'href="privacy-policy\.html"': 'href="/privacy-policy"',
    r'href="terms-conditions\.html"': 'href="/terms-conditions"',
    r'href="preschool-gachibowli\.html"': 'href="/preschool-gachibowli"',
    r'href="preschool-nallagandla\.html"': 'href="/preschool-nallagandla"',
    r'href="preschool-attapur\.html"': 'href="/preschool-attapur"',
    r'href="preschool-begumpet\.html"': 'href="/preschool-begumpet"',
    r'href="preschool-ameerpet\.html"': 'href="/preschool-ameerpet"',
}

count = 0
for filename in html_files:
    filepath = Path(filename)
    if not filepath.exists():
        print(f"⚠️  Skipping {filename} - not found")
        continue
    
    content = filepath.read_text(encoding='utf-8')
    original_content = content
    
    # Apply all replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    
    # Save if changed
    if content != original_content:
        filepath.write_text(content, encoding='utf-8')
        changes = sum(1 for p in replacements.keys() if re.search(p, original_content))
        print(f"✅ Fixed {filename} - {changes} patterns replaced")
        count += 1
    else:
        print(f"ℹ️  {filename} - already fixed")

print(f"\n🎉 Complete! Fixed {count} files with clean URL links")
