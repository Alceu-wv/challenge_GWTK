import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


def test_get_most_popular_pizza(api, mocker, pizza_and_quantity):
    # Arrange
    pizza, quantity = pizza_and_quantity
    mocker.patch("main_app.views.statistics.get_most_popular_pizza", return_value=pizza_and_quantity)

    # Act
    req = api.get("/api/get_most_popular_pizza/")

    # Assert
    assert req.status_code == 200
    assert req.json() == {
        "pizza": model_to_dict(pizza),
        "quantity": quantity,
    }


def test_get_most_popular_pizza_no_data(api):

    req = api.get("/api/get_most_popular_pizza/")

    assert req.status_code == 200
    assert req.json() == {"detail": "No data, impossible do generate statistic for most popular pizza"}


# TODO: Same structure than get_most_popular_pizza testing
def test_get_most_sold_pizzas(api):
    pass


def test_get_most_sold_pizzas_no_data(api):
    pass


# TODO: Same structure than get_most_popular_pizza testing
def test_get_most_popular_pizza_day(api):
    pass


def test_get_most_popular_pizza_day_no_data(api):
    pass


# TODO: Same structure than get_most_popular_pizza testing
def test_get_most_popular_pizza_ingredients(api):
    pass


def test_get_most_popular_pizza_ingredients_no_data(api):
    pass
