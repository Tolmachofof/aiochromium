import os
import re
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

from aiochromium.domains.dom import DOM


def convert_to_snake_case(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def get_domain_attribute_name(attribute_name):
    return '_' + convert_to_snake_case(attribute_name).upper()


def test_dom_domain_implements_all_commands(dom_protocol):
    for command in filter(
            lambda item: not item.get('experimental', False),
            dom_protocol['commands']
    ):
        dom_attribute_name = get_domain_attribute_name(command['name'])
        assert hasattr(DOM, dom_attribute_name)
        assert getattr(DOM, dom_attribute_name)[0] == 'DOM.' + command['name']
