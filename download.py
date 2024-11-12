import instaloader
import os
import sys
import zipfile

def download_profile(username, zip_enabled=False):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Download the profile
        print(f"Starting download for profile: {username}...")
        L.download_profile(username, profile_pic_only=False)

        # If zip_enabled is True, zip the downloaded files
        if zip_enabled:
            zip_directory(username)

        print(f"Download completed for profile: {username}.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"Profile '{username}' is private and not followed.")
    except Exception as e:
        print(f"An error occurred while downloading the profile: {e}")

def zip_directory(username):
    folder_path = os.path.join(os.getcwd(), username)
    zip_file_path = f"{username}.zip"

    # Create a zip file
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), folder_path))

    print(f"Zipped files for '{username}' into '{zip_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download.py <username> [--zip]")
        sys.exit(1)

    username = sys.argv[1]
    zip_enabled = '--zip' in sys.argv

    download_profile(username, zip_enabled)
