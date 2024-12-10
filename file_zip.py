import os
import re
import zipfile
from shutil import move

def zip_and_move_pdfs(source_folder, destination_folder):
    """
    Finds PDF files in the source folder, groups them based on 'x' value in the naming pattern `abc_x_y`,
    zips the groups, and moves the zip files to the destination folder.

    Args:
        source_folder (str): Path to the folder containing the source PDF files.
        destination_folder (str): Path to the folder to store the zip files.
    """
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Regex to match files named in the pattern abc_x_y.pdf
    file_pattern = re.compile(r"abc_(\d+)_(\d+)\.pdf")

    # Dictionary to group files by 'x' value
    grouped_files = {}

    # Scan source folder
    for filename in os.listdir(source_folder):
        match = file_pattern.match(filename)
        if match:
            x_value = int(match.group(1))  # Extract 'x' value
            grouped_files.setdefault(x_value, []).append(filename)

    # Process each group
    for x_value, files in grouped_files.items():
        zip_filename = f"abc_{x_value}_group.zip"
        zip_path = os.path.join(destination_folder, zip_filename)

        # Create a zip file for the group
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                file_path = os.path.join(source_folder, file)
                zipf.write(file_path, arcname=file)  # Add file to zip

        print(f"Zipped group {x_value} into: {zip_path}")

if __name__ == "__main__":
    # Define source and destination folder paths
    source_folder = "path/to/source/folder"  # Replace with your source folder path
    destination_folder = "path/to/destination/folder"  # Replace with your destination folder path

    # Execute the function
    zip_and_move_pdfs(source_folder, destination_folder)

