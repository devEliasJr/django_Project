import re

from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')

    if not regex.match(password):
        raise ValidationError((
            'A senha deve conter no minimo 6 digitos, '
            'letra maiuscula, minusculas e um numero'
        ),
            code='Invalid')


def email_validation(email):
    email_regex = re.compile(
        r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

    if not email_regex.match(email):
        raise ValidationError((
            'digite um email válido'
        ),
            code='Invalid')
