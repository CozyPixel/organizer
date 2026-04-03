import os
import shutil

# 1. Paths to your standard Windows folders.
# IMPORTANT: Replace 'YourUsername' with your actual Windows YourUsernamename in all paths!
DOWNLOADS_DIR = r'C:\Users\YourUsername\Downloads'
PICTURES_DIR  = r'C:\Users\YourUsername\OneDrive\Pictures'
DOCUMENTS_DIR = r'C:\Users\YourUsername\OneDrive\Documents'
VIDEOS_DIR    = r'C:\Users\YourUsername\Videos'
MUSIC_DIR     = r'C:\Users\YourUsername\Music'

# 2. Sorting rules: target folder path and matching file extensions
FOLDERS_SCHEMA = {
    PICTURES_DIR: ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'],
    DOCUMENTS_DIR: ['.pdf', '.docx', '.xlsx', '.txt', '.pptx', '.csv'],
    VIDEOS_DIR: ['.mp4', '.avi', '.mkv', '.mov'],
    MUSIC_DIR: ['.mp3', '.wav', '.flac']
}

def organize():
    # Check if the Downloads folder actually exists
    if not os.path.exists(DOWNLOADS_DIR):
        print("Folder not found! Please check the path to your Downloads folder.")
        return

    print("Starting cleanup...")
    
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        
        # We skip folders and only move files
        if not os.path.isfile(file_path):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        for target_folder, extensions in FOLDERS_SCHEMA.items():
            if file_ext in extensions:
                # Check if the target Windows folder exists (just in case)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder, exist_ok=True)
                
                target_path = os.path.join(target_folder, filename)
                
                # Move the file to the standard Windows folder
                shutil.move(file_path, target_path)
                print(f"Moved: {filename} -> {target_folder}")
                moved = True
                break
        
        # Files with unknown extensions (like .exe or .zip) will stay in Downloads.
        # This keeps your main folders clean from random files.
        if not moved:
            print(f"Skipped (unknown type): {filename}")

    print("Cleanup complete! Files have been moved to your standard Windows folders.")

if __name__ == "__main__":
    organize()