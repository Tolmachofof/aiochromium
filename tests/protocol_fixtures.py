import os
import json

import pytest


@pytest.yield_fixture
def protocol():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, 'browser_protocol.json')) as f:
        yield json.load(f)


@pytest.fixture
def dom_protocol(protocol):
    return list(
        filter(lambda domain: domain['domain'] == 'DOM', protocol['domains'])
    )[0]
