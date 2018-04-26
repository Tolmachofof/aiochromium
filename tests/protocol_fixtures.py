import os
import json

import pytest

from aiochromium.domains.base import Array, String, Integer


@pytest.yield_fixture
def protocol():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, 'browser_protocol.json')) as f:
        yield json.load(f)


@pytest.fixture
def mapped_protocol_types():
    return {
        'array': Array,
        'integer': Integer,
        'string': String
    }


@pytest.fixture
def dom_protocol(protocol):
    return list(
        filter(lambda domain: domain['domain'] == 'DOM', protocol['domains'])
    )[0]


@pytest.fixture
def page_protocol(protocol):
    return list(
        filter(lambda domain: domain['domain'] == 'Page', protocol['domains'])
    )[0]


@pytest.fixture
def get_domain_stable_methods():
    def get_stable_methods(domain):
        for method in filter(
                # Return only stable methods (not experimental)
                lambda item: not item.get('experimental', False),
                domain['commands']
        ):
            yield method
    return get_stable_methods
