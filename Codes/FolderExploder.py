import os
import shutil

# --- CONFIGURATION ---
# This targets the "Target" folder inside your Downloads
FOLDER_TO_EXPLODE = os.path.join(os.path.expanduser("~"), "Downloads", "Software")
# ---------------------

def explode_folder():
    # 1. Check if the "Target" folder actually exists
    if not os.path.exists(FOLDER_TO_EXPLODE):
        print(f"Error: The folder '{FOLDER_TO_EXPLODE}' does not exist.")
        return

    # 2. Determine the "Parent" folder (which is Downloads)
    parent_folder = os.path.dirname(FOLDER_TO_EXPLODE)
    
    print(f"Moving contents from:\n  {FOLDER_TO_EXPLODE}\nTo:\n  {parent_folder}\n")

    # 3. Move the files
    files_moved = 0
    items = os.listdir(FOLDER_TO_EXPLODE)
    
    if not items:
        print("Folder is already empty.")
    
    for item in items:
        source_path = os.path.join(FOLDER_TO_EXPLODE, item)
        destination_path = os.path.join(parent_folder, item)

        try:
            # Check if file already exists in Downloads to prevent overwriting
            if os.path.exists(destination_path):
                print(f"⚠️ SKIPPED: {item} (File with this name already exists in Downloads)")
            else:
                shutil.move(source_path, destination_path)
                print(f"✅ Moved: {item}")
                files_moved += 1
        except Exception as e:
            print(f"❌ Error moving {item}: {e}")

    # 4. Remove the empty 'Target' folder
    # We check os.listdir again to make sure we didn't skip any files
    if not os.listdir(FOLDER_TO_EXPLODE):
        try:
            os.rmdir(FOLDER_TO_EXPLODE)
            print(f"\n🎉 Success! The folder has been deleted.")
        except OSError as e:
            print(f"Error deleting folder: {e}")
    else:
        print("\n⚠️ Could not delete the folder because some items (skipped files) are still inside.")

if __name__ == "__main__":
    explode_folder()