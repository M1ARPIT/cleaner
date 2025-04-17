import os
import shutil
import time

# Folder to clean
folder_to_clean = "E:\documents"

# Destination folders for organized files
folders_by_type = {
    "images": "E:/organized/images",
    "documents": "E:/organized/documents",
    "videos": "E:/organized/videos",
    "others": "E:/organized/others"
}

# File extensions for categories
file_types = {
    "images": [".jpg", ".png", ".jpeg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".mov", ".avi"]
}

# File age limit (e.g., 2 years in seconds)
file_age_limit = 2 * 365 * 24 * 60 * 60  # 2 years

# Ensure destination folders exist
for folder in folders_by_type.values():
    os.makedirs(folder, exist_ok=True)

def clean_folder():
    current_time = time.time()
    
    for filename in os.listdir(folder_to_clean):
        file_path = os.path.join(folder_to_clean, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Delete old files
        file_age = current_time - os.path.getmtime(file_path)
        if file_age > file_age_limit:
            print(f"Deleting old file: {filename}")
            os.remove(file_path)
            continue

        # Move files based on their extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                dest_path = os.path.join(folders_by_type[category], filename)
                shutil.move(file_path, dest_path)
                print(f"Moved {filename} to {dest_path}")
                moved = True
                break

        # Move uncategorized files to "others"
        if not moved:
            dest_path = os.path.join(folders_by_type["others"], filename)
            shutil.move(file_path, dest_path)
            print(f"Moved {filename} to {dest_path}")

if __name__ == "__main__":
    print("Starting folder cleaner...")
    clean_folder()
    print("Folder cleaning completed!")
