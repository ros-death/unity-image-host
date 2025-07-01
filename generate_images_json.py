import os
import json
import re

# makes the JSONs in the slides folders!
root_folder = "./"  # Adjust if your images folders are in a subfolder

def extract_number(filename):
    # Extract number after 'slide' prefix, e.g. slide12.png -> 12
    match = re.search(r'slide(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return float('inf')  # put non-matching files at the end

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            # Sort files based on the extracted number
            image_files.sort(key=extract_number)

            json_path = os.path.join(folder_path, "images.json")
            with open(json_path, 'w') as json_file:
                json.dump(image_files, json_file, indent=2)
            print(f"Created images.json in {folder_path}")
