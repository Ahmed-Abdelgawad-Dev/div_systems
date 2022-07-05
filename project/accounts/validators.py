import os
from django.core.exceptions import ValidationError


def validate_avatar(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg''.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Please upload images of type { jpg, jpeg, png } only.')
