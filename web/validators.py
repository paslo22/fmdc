import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    # First value is path + filename
    _, extension = os.path.splitext(value.name).lower()
    valid_extensions = ['.mp4']
    if extension not in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
