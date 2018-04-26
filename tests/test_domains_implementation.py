import os
import sys
from unittest import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

from aiochromium.domains.base import Array, Integer, String
from aiochromium.domains.dom import (
    BackendNode, BoxModel, DOM, Node, RGBA, ShapeOutsideInfo, Rect
)
from aiochromium.utils.naming_transformer import camel_case_to_snake_case


def get_domain_attribute_name(attribute_name):
    return '_' + camel_case_to_snake_case(attribute_name).upper()


def get_method_params(domain_method, mapped_types):
    if 'returns' in domain_method:
        wrapper_name = (
            domain_method['returns'][0].get('type')
            or domain_method['returns'][0]['$ref']
        )
        source = domain_method['returns'][0]['name']
        target = (
            domain_method['returns'][0]['items']['$ref']
            if 'items' in domain_method else None
        )
        method_params = {
            'wrapper_class': mapped_types.get(wrapper_name, None),
            'source': source,
            'target': target
        }
        return {
            param: value for param, value in method_params.items()
            if value is not None
        }
    else:
        return {}


def test_domain_dom_implements_all_methods_from_protocol(
    dom_protocol, get_domain_stable_methods
):
    for method in get_domain_stable_methods(dom_protocol):
        dom_attribute_name = get_domain_attribute_name(method['name'])
        assert hasattr(DOM, dom_attribute_name)
        assert getattr(DOM, dom_attribute_name) == 'DOM.' + method['name']
        assert hasattr(DOM, camel_case_to_snake_case(method['name']))


def test_domain_dom_methods_implements_all_params_from_protocol(
    dom_protocol, get_domain_stable_methods, mapped_protocol_types
):
    mapped_dom_types = {
        'NodeId': Integer,
        'BackendNodeId': Integer,
        'BackendNode': BackendNode,
        'PseudoType': String,
        'ShadowRootType': String,
        'Node': Node,
        'RGBA': RGBA,
        'Quad': Array,
        'BoxModel': BoxModel,
        'ShapeOutsideInfo': ShapeOutsideInfo,
        'Rect': Rect
    }
    mapped_dom_types.update(mapped_protocol_types)
    with mock.patch.object(DOM, 'create_frame', autospec=True) as frame_mock:
        for method in get_domain_stable_methods(dom_protocol):
            expected_params = {
                param['name']: param['name']
                for param in method.get('parameters', [])
            }
            # Call domain method with params
            getattr(DOM, camel_case_to_snake_case(method['name']))(
                **{
                    camel_case_to_snake_case(name): value
                    for name, value in expected_params.items()
                }
            )
            call_args, call_kwargs = frame_mock.call_args
            assert call_args, call_kwargs == (
                (
                    getattr(DOM, get_domain_attribute_name(method['name'])),
                    expected_params
                ),
                expected_params
            )
