from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')


def validate_description(value):
    if len(value) < 10:
        raise ValidationError('Deskripsi harus memiliki minimal 10 karakter.')
    if len(value) > 300:
        raise ValidationError('Deskripsi tidak boleh lebih dari 300 karakter.')
