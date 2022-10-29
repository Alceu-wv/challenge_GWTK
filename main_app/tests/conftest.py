import pytest
from rest_framework.test import APIClient

from main_app.models import Order
from main_app.models.pizza_type import PizzaType
from main_app.models.pizzas import Pizzas


@pytest.fixture
def api():
    client = APIClient(HTTP_AUTHORIZATION="token foo")
    return client


@pytest.fixture
def order():
    return Order.objects.create(**{"id": 1, "date": "2015-01-01", "time": "11:38:36"})


@pytest.fixture
def pizza_type():
    return PizzaType.objects.create(
        **{
            "id": "bbq_ckn",
            "name": "The Barbecue Chicken Pizza",
            "category": "Chicken",
            "ingredients": "Barbecued Chicken",
        }
    )


@pytest.fixture
def pizza():
    return Pizzas.objects.create(**{"id": "hawaiian_m", "pizza_type_id": "bbq_ckn", "price": 12.75})
