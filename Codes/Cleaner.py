import os
import shutil

# 1. Define the path to your Downloads folder
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# 2. Updated Map based on your specific request
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tiff", ".ico"],
    "Documents": [".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".accdb", ".rtf"],
    "PDFs": [".pdf"],
    "Compressed Files": [".zip", ".rar", ".7z", ".tar", ".gz", ".pkg"],
    "Program Installers": [".exe", ".msi", ".dmg", ".iso", ".bin", ".setup"]
}

def clean_folder():
    # Check every item in the downloads folder
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)

        # Skip if it's a directory (we only want to move files)
        if os.path.isdir(file_path):
            continue

        # Get the file extension (e.g., ".pdf")
        _, extension = os.path.splitext(filename)
        extension = extension.lower() # Make sure it's lowercase to match our list
        
        # Default destination is "Others"
        target_folder_name = "Others"

        # Check if the file belongs to a known category
        for category, extensions_list in FILE_CATEGORIES.items():
            if extension in extensions_list:
                target_folder_name = category
                break
        
        # --- Perform the Move ---
        # Define the full path for the destination folder
        target_folder = os.path.join(downloads_path, target_folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"Created new folder: {target_folder_name}")

        # Move the file
        try:
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved: {filename} -> {target_folder_name}/")
        except shutil.Error:
            print(f"Skipped: {filename} (File already exists in {target_folder_name})")
        except Exception as e:
            print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    print(f"--- Organizing {downloads_path} ---")
    clean_folder()
    print("--- Cleanup Complete ---")