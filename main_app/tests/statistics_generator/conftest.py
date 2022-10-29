import pandas as pd
import pytest


@pytest.fixture
def df_popularity_rank(pizza, pizza_type):
    d = {"index": pizza.id, "quantity": [10]}
    df = pd.DataFrame(data=d)
    df.set_index("index", inplace=True)
    return df
