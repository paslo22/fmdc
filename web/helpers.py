Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@manuel14 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


paslo22
/
fmdc
2
00
 Code Issues 0 Pull requests 1 Actions Projects 0 Wiki Security Insights
fmdc/web/helpers.py / 
 Manuel Zubieta Uploading new sections and test
3240187 5 minutes ago
78 lines (62 sloc)  2.05 KB
 
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more


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
    if not os.path.exists(lookup_path):
        create_folder(path=lookup_path)
    for filepath in os.listdir(lookup_path):
        image_extension_pattern_compiled = re.compile(pattern)
        try:
            filename = re.match(image_extension_pattern_compiled, filepath).group(1)
            file_in_path = {
                'url': settings.MEDIA_URL + path + filepath,
                'name': filename
            }
            if pattern == IMAGE_EXTENSION_PATTERN:
                height, width = get_width_and_height_from_image(path=lookup_path + filepath)
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
    except FileNotFoundError:
        raise


def copy_tmp_file_into_destination(tmp_file, destination_file):
    with open(destination_file, 'wb+') as destination:
        for chunk in tmp_file:
            destination.write(chunk) 
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
