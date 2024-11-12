import os
import zipfile

def zip_directory(directory_path, zip_file_path):
    """
    Zips the contents of the specified directory.

    :param directory_path: Path to the directory to zip.
    :param zip_file_path: Path where the zip file will be saved.
    """
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Create a relative path for the file to maintain directory structure
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=directory_path)
                zipf.write(file_path, arcname)

    print(f"Zipped directory '{directory_path}' into '{zip_file_path}'.")

def main():
    # Example usage
    directory_to_zip = input("Enter the directory to zip: ")
    zip_file_name = input("Enter the name for the zip file (without extension): ")
    zip_file_path = f"{zip_file_name}.zip"

    if os.path.isdir(directory_to_zip):
        zip_directory(directory_to_zip, zip_file_path)
    else:
        print(f"The directory '{directory_to_zip}' does not exist.")

if __name__ == "__main__":
    main()
