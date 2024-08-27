import winreg
import os
import zipfile

def extract_zip(zip_path, extract_to):
    try:
        # Ensure the destination directory exists
        os.makedirs(extract_to, exist_ok=True)
        
        # Open the .zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files to the destination directory
            zip_ref.extractall(extract_to)
            print(f"Files extracted to {extract_to}")
    except zipfile.BadZipFile as e:
        print(f"Error: Bad .zip file {e}")
    except Exception as e:
        print(f"Error extracting .zip file: {e}")

def copy_file(source_path, destination_path):
    try:
        # Open the source file in binary read mode
        with open(source_path, "rb") as src_file:
            # Read the source file's content
            file_data = src_file.read()
        
        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Open the destination file in binary write mode
        with open(destination_path, "wb") as dest_file:
            # Write the content to the destination file
            dest_file.write(file_data)
        
        print(f"File copied from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying file: {e}")

def get_absolute_path(relative_path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path
    absolute_path = os.path.join(script_dir, relative_path)
    return absolute_path

if __name__ == "__main__":
    os.chdir("../")
    os.system("cargo build --release")

    copy_file(get_absolute_path("./../target/release/RustSDelete.exe"), "C:/RustSDelete/RustSDelete.exe")

    extract_zip(get_absolute_path("./../SDelete/SDelete.zip"), "C:/RustSDelete/SDelete/")
