import os
import shutil

# Source folder (where images are)
source_folder = "C:\\Users\\khana\\OneDrive\\Desktop\\source img"

# Destination folder (where images will go)
destination_folder = "C:\\Users\\khana\\OneDrive\\Desktop\\destination im"

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files in source folder
for file_name in os.listdir(source_folder):
    # Check if file is a .jpg image
    if file_name.endswith(".jpg"):
        full_file_path = os.path.join(source_folder, file_name)
        
        # Move file to destination folder
        shutil.move(full_file_path, destination_folder)
        print(f"Moved: {file_name}")

print("Task Completed!")

