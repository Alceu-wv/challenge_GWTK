import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def df_order_details(order, pizza_type, pizza):
    return pd.read_csv("main_app/tests/parsers/csv_samples/order_details.csv", encoding="unicode_escape")


@pytest.fixture
def df_order_details_repeated_element(order, pizza_type, pizza):
    data = []
    [data.append([1, 1, "hawaiian_m", 1]) for x in range(5)]
    return pd.DataFrame(np.array(data), columns=["order_details_id", "order_id", "pizza_id", "quantity"])
