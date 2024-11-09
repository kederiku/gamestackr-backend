import pytest
from django.test import override_settings


@pytest.fixture(autouse=True)
def test_settings(settings):
    with override_settings(SECRET_KEY='y8)@n0129*-4)wmq5eal-(lds@h&md_%%xj95g1a!_1p=mq=b7',):
        yield
