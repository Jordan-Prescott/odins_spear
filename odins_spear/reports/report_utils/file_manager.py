import os
import json

import shutil

from ...exceptions import OSFileNotFound


def check_directory_or_file_exists(directory_file_path: str) -> bool:
    """Checks if a directory or file exists.

    Args:
        directory_file_path (str): Path to the directory or file.

    Returns:
        bool: If path exists return True else False.
    """

    if os.path.exists(directory_file_path):
        return True

    return False


def join_path(directory: str, file_name: str) -> str:
    """Using os.path this method joins directory with file name and normalises path
    for the OS running on.

    Args:
        directory (str): Directory path.
        file_name (str): Name of file.

    Returns:
        str: Returns normalised string of joined path.
    """

    return os.path.normpath(os.path.join(directory, file_name))


def json_fie_to_dict(file_path: str) -> dict:
    """Loads a json file into code as Python dict.

    Args:
        file_path (str): Path to json file including file name.

    Returns:
        dict: Python dict of json file. Returns False if file not found.

    Raises:
        OSFileNotFound: Raised when file cant found.
    """

    if check_directory_or_file_exists(file_path):
        with open(file_path, "r") as data:
            return json.loads(data.read())

    return OSFileNotFound


def make_directory(directory_path: str) -> None:
    """Checks if directory already exists if not it will create it.

    Args:
        directory_path (str): Path to target directory.

    Returns:
        None: Function builds directory.
    """

    return os.makedirs(directory_path, exist_ok=True)


def copy_all_directorys_files_to_target(source_dir, target_dir) -> bool:
    """

    Args:
        source_dir (_type_): _description_
        target_dir (_type_): _description_

    Returns:
        bool: Returns True if operation succeeded.

    Raises:
        OSFileNotFound: Raised when source directoty can't be found.
    """

    if check_directory_or_file_exists(source_dir):
        # Check if target dir exists if not build it
        make_directory(target_dir)

        # Copy files
        shutil.copytree(source_dir, target_dir)
        return True

    return OSFileNotFound


def copy_single_file_to_target_directory(
    source_dir: str, target_dir: str, file_name: str
) -> bool:
    """Copies a single targeted file from a source directory to a target directory.

    Args:
        source_dir (str): Source directory path where target file is located.
        target_dir (str): Target directory path where target file is to be copied to.
        file_name (str): Name of source file

    Returns:
        bool: Returns True if operation succeeded.

    Raises:
        OSFileNotFound: Raised when source target file can't be found.
    """

    # Construct the full paths using os.path.join and normalize them
    source_file = os.path.normpath(os.path.join(source_dir, file_name))
    target_file = os.path.normpath(os.path.join(target_dir, file_name))

    if check_directory_or_file_exists(source_file):
        # Create the target directory if it does not exist
        os.makedirs(target_dir, exist_ok=True)

        # Copy the file to the target directory
        shutil.copy2(source_file, target_file)
        return True

    return OSFileNotFound


def remove_directory(directory_path: str) -> bool:
    """Check if file exists and type is directory and if both are true the directory is removed.

    Args:
        directory_path (str): Path to target directory to be removed.

    Returns:
        bool: _description_
    """

    if check_directory_or_file_exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        return True

    return False
