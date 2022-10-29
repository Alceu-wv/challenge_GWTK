from typing import Tuple

import numpy as np
import pandas as pd

from main_app.models import Pizzas


def get_popularity_rank(df: pd.DataFrame) -> pd.DataFrame:

    """Input a query dataframe from table <<OrderDetails>> to get an ordered dataframe of most ordered pizzas"""

    df_popularity_rank = df[["pizza_id", "quantity"]].groupby("pizza_id").count()
    df_popularity_rank.sort_values("quantity", ascending=False, inplace=True)
    return df_popularity_rank


def get_most_ordered_pizza_and_quantity(df: pd.DataFrame) -> Tuple[Pizzas, np.int64]:

    """Input a query dataframe from table <<OrderDetails>> to get most ordered pizza and how many times was it ordered"""

    df = get_popularity_rank(df)

    pizza_id = df.index[0]
    quantity = df.quantity[0]

    pizza = Pizzas.objects.get(id=pizza_id)

    return pizza, quantity
