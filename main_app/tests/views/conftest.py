import pytest


@pytest.fixture
def pizza_and_quantity(pizza, pizza_type):
    return pizza, 1
