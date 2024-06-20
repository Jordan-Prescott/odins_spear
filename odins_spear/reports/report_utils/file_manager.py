import os
import json

import shutil


def check_directory_or_file_exists(directory_file_path: str) -> bool:

    if os.path.exists(directory_file_path):
        return True
    
    return False ##TODO: return error or notify in someway


def json_fie_to_dict(file_path: str) -> dict:
    """Takes path to JSON file and loads file into Python Dict Object.

    :param path: Path to file that will be loaded into Python Dict Object.
    :return: Python Dict object.
    """
    if check_directory_or_file_exists(file_path):
        with open(file_path, 'r') as data:
            return json.loads(data.read())
    
    return False #TODO: return error or notify in someway
    

def make_directory(directory_path) -> bool:
    """takes in a path and creates a new directory if dir does not already exist

    :param path: Path to directory.
    :return: Returns True to indicate complete.
    """

    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
        return True

    return False ##TODO: return error or notify in someway


def copy_all_directorys_files_to_target(source_dir, target_dir) -> bool:
    """takes in source directory and new target directory which will copy all files from source, create new target
    directory and paste all files into new directory.

    :param source_dir: Directory where source files are located.
    :param target_dir: Directory which will be created and source files copied to.
    :return: Returns True to indicate complete.
    """
    
    if check_directory_or_file_exists(source_dir) and check_directory_or_file_exists(target_dir):
        shutil.copytree(source_dir, target_dir)
        return True
    
    return False #TODO: return error or notify in someway


def copy_single_file_to_target_directory(source_dir, target_dir, file_name) -> bool:
    """Copies a single targeted file from the source directory to the specified target directory.

    :param source_dir: Directory where the source file is located.
    :param target_dir: Directory where the file will be copied to.
    :param file_name: Name of the file to be copied.
    :return: Returns True to indicate the file was successfully copied.
    """
    
    source_dir = os.path.normpath(source_dir)
    
    # Construct the full paths using os.path.join and normalize them
    source_file = os.path.normpath(os.path.join(source_dir, file_name))
    target_file = os.path.normpath(os.path.join(target_dir, file_name))
    
    if os.path.isfile(source_file):
        # Create the target directory if it does not exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Copy the file to the target directory
        shutil.copy2(source_file, target_file)
        return True
    else:
        print(f"Source file {source_file} does not exist.")
        return False
    
    return False  # Return False if the source file does not exist


def remove_directory(directory_path) -> bool:
    """takes in path to directory which will be removed if found and path given is a direactory.
    If path given an error will be raised to indicate path cant be found. 
    """

    if check_directory_or_file_exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        return True
    
    return False