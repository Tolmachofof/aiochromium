import re


def camel_case_to_snake_case(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def snake_case_to_camel_case(name):
    first, *tail = name.split('_')
    return first + ''.join(word.capitalize() for word in tail)
