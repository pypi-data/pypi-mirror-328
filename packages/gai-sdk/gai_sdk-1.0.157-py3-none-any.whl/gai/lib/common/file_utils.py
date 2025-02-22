import os, zipfile
import tempfile,shutil
import mimetypes

def is_binary(file_name):
    mime_type, encoding = mimetypes.guess_type(file_name)
    return mime_type.startswith('text') if mime_type else False

# Remove most non-alphanumeric characters from a filename
def clean_paths(file_path_or_paths):
    if (isinstance(file_path_or_paths,list)):
        paths = []
        for file_path in file_path_or_paths:
            paths.append(clean_paths(file_path))
        return paths
    return file_path_or_paths.replace("/","_").replace("\\","_").replace(" ","_").replace(":","").replace(",","").replace("'","").replace('"','').lower()

# Return all files in a directory and its subdirectories as a list of absolute paths
def flatten_abs_paths(dir_or_file):
    abs_file_paths = []
    if os.path.isfile(dir_or_file):
        abs_file_paths.append(os.path.abspath(dir_or_file))
        return abs_file_paths
    
    for dirpath, _, filenames in os.walk(dir_or_file):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            abs_file_paths.append(os.path.abspath(file_path))
    return abs_file_paths

## FILE ZIP FUNCTIONS

def unzip_and_remove(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)  # remove the .zip file after extraction

def _unzip_temp(temp_dir):
    for root, dirs, files in os.walk(temp_dir):
        for filename in files:
            if filename.endswith(".zip"):
                zip_file_path = os.path.join(root, filename)
                unzip_and_remove(zip_path=zip_file_path, extract_to=root)
                _unzip_temp(root) # recursive call to handle nested zip files

def unzip_all(file_or_dir, dest_dir=None):
    # Copy all into a temp dir
    temp_dir = tempfile.mkdtemp()
    shutil.copytree(file_or_dir, temp_dir, dirs_exist_ok=True)

    # Recursively unzip zipped files
    _unzip_temp(temp_dir)

    # Move all files to dest_dir (if exists)
    if dest_dir:
        shutil.copytree(temp_dir, dest_dir, dirs_exist_ok=True)
        shutil.rmtree(temp_dir)
        return dest_dir
    
    return temp_dir

