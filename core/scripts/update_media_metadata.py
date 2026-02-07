import os
import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Target pattern: src: "../images/thumbs/..."
    # Only if inside MediaMetadata / artwork block
    # We can just look for the specific thumb paths which are unique to our player
    
    modified = False
    
    # Pattern to find relative thumb paths in src properties
    pattern = r'src:\s*"((\.\./)+images/thumbs/[^"]+)"'
    
    def replacer(match):
        path = match.group(1)
        return f'src: new URL("{path}", window.location.href).href'

    # Special case for files that already have manual fixes or different structures (like index)
    if "index.html" in filepath:
        return
        
    new_content = re.sub(pattern, replacer, content)
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

directories = [
    "core/data/main/podcast",
    "core/data/cowork/podcast",
    "core/data/meta/podcast"
]

for d in directories:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html"):
                update_file(os.path.join(d, filename))
