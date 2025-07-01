import os
import json

root_folder = "./"  # Adjust if your images folders are in a subfolder

for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    if os.path.isdir(folder_path):
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if image_files:
            json_path = os.path.join(folder_path, "images.json")
            with open(json_path, 'w') as json_file:
                json.dump(image_files, json_file, indent=2)
            print(f"Created images.json in {folder_path}")
