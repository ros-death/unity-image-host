import os
import json

root_folder = "./"  # Adjust if your images folders are in a subfolder

folders_with_images = []

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            # Add folder name to list
            folders_with_images.append(folder_name)

            # Write images.json as before
            json_path = os.path.join(folder_path, "images.json")
            with open(json_path, 'w') as json_file:
                json.dump(sorted(image_files), json_file, indent=2)
            print(f"Created images.json in {folder_path}")

# Write folders.json in root
folders_json_path = os.path.join(root_folder, "folders.json")
with open(folders_json_path, 'w') as folders_file:
    json.dump(sorted(folders_with_images), folders_file, indent=2)
print(f"Created folders.json in {root_folder}")
