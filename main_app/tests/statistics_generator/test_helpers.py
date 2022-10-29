import numpy
import pandas as pd
import pytest

from main_app.statistics_generator.helpers import get_most_ordered_pizza_and_quantity

pytestmark = pytest.mark.django_db


def test_get_sorted_pizza(mocker, pizza, df_popularity_rank):
    mocker.patch("main_app.statistics_generator.helpers.get_popularity_rank", return_value=df_popularity_rank)

    res_pizza, quantity = get_most_ordered_pizza_and_quantity(pd.DataFrame)

    assert res_pizza == pizza
    isinstance(quantity, numpy.int64)
    assert quantity == 10


def test_get_popularity_rank():
    pass
