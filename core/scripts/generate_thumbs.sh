#!/bin/bash

# Find all front and back covers
find . -name "*_audiobook_cover_front.png" -o -name "*_audiobook_cover_back.png" -o -name "*_abook_cover_front.png" -o -name "*_abook_cover_back.png" | while read -r file; do
    dir=$(dirname "$file")
    filename=$(basename "$file")
    extension="${filename##*.}"
    filename_no_ext="${filename%.*}"
    
    # Define new filename with _thumb suffix
    thumbs_dir="$dir/thumbs"
    mkdir -p "$thumbs_dir"
    thumb_name="${filename_no_ext}_thumb.${extension}"
    thumb_path="$thumbs_dir/$thumb_name"

    # Check if thumb already exists (optional: overwrite logic)
    # We will overwrite to ensure latest version
    echo "Processing $file -> $thumb_path"
    
    # Resize to 400px width (for retina 200px display)
    convert "$file" -resize 400x "$thumb_path"
done

echo "Thumbnail generation complete."
