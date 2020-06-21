
import re
import os
from PIL import Image

from django.conf import settings

from web.constants import IMAGE_EXTENSION_PATTERN


def get_files_from_folder_path(path, pattern):
    """
    Travels through a directory and returns all the images in it

    Args:
        path: str: path in the system from where to look for the files
        pattern: str: regex to match files

    Returns:
        list: list of files that were found in the path and matched the regex pattern
    """
    files = []
    # Path where to look for files
    lookup_path = settings.MEDIA_ROOT + path
    if not os.path.exists(lookup_path.encode()):
        create_folder(path=lookup_path)
    for filepath in os.listdir(lookup_path.encode()):
        image_extension_pattern_compiled = re.compile(pattern)
        try:
            filename = re.match(image_extension_pattern_compiled, filepath.decode("utf-8")).group(1)
            file_in_path = {
                'url': ''.join([settings.MEDIA_URL[0:-1], path, filepath.decode("utf-8")]),
                'name': filename
            }
            if pattern == IMAGE_EXTENSION_PATTERN:
                try:
                    height, width = get_width_and_height_from_image(path=lookup_path + filepath.decode("utf-8"))
                except Exception:
                # could not read image
                    continue
                file_in_path['width'] = width
                file_in_path['height'] = height
            files.append(file_in_path)
        except AttributeError:
            # file does not match the extension wanted so we ignore it
            continue
    return files


def create_folder(path):
    """
    Args:
        path: str: path like object

    """
    try:
        os.makedirs(path)
    except PermissionError:
        raise


def get_width_and_height_from_image(path):
    """
    Args:
        path: str: path to the image

    Returns:
        tuple: (height, width) of image
    """
    try:
        opened_file = Image.open(path)
        width, height = opened_file.size
        return (height, width)
    except OSError:
        raise


def copy_tmp_file_into_destination(tmp_file, destination_file):
    with open(destination_file, 'wb+') as destination:
        for chunk in tmp_file:
            destination.write(chunk) 


def safe_unicode_str(string):
    """
    Args
        string: string you want to safe encode

    Returns
        str: safely converted string to avoid UnicodeEncodeErrors
    """
    return string.encode('utf-8', 'surrogateescape').decode()