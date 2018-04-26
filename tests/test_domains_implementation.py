import os
import sys
from unittest import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

from aiochromium.domains.dom import DOM
from aiochromium.utils.naming_transformer import camel_case_to_snake_case


def get_domain_attribute_name(attribute_name):
    return '_' + camel_case_to_snake_case(attribute_name).upper()


def test_domain_dom_implements_all_methods_from_protocol(
    dom_protocol, get_domain_stable_methods
):
    for method in get_domain_stable_methods(dom_protocol):
        dom_attribute_name = get_domain_attribute_name(method['name'])
        assert hasattr(DOM, dom_attribute_name)
        assert getattr(DOM, dom_attribute_name) == 'DOM.' + method['name']
        assert hasattr(DOM, camel_case_to_snake_case(method['name']))


def test_domain_dom_methods_implements_all_params_from_protocol(
    dom_protocol, get_domain_stable_methods
):
    with mock.patch.object(DOM, 'create_frame') as frame_mock:
        for method in get_domain_stable_methods(dom_protocol):
            method_params = {
                camel_case_to_snake_case(param['name']): param['name']
                for param in method.get('parameters', [])
            }
            # Call domain method with params
            getattr(DOM, camel_case_to_snake_case(method['name']))(
                **method_params
            )
            assert frame_mock.called_with(
                getattr(DOM, get_domain_attribute_name(method['name'])),
                method_params
            )
