import datetime
from typing import Tuple

import numpy as np
import pandas as pd

from main_app.exceptions import NoDataException
from main_app.models import Order, OrderDetails, Pizzas
from main_app.statistics_generator.helpers import get_most_ordered_pizza_and_quantity


def get_most_popular_pizza_day() -> Tuple[datetime.date, Pizzas, np.int64]:

    """
    Using popularity insights from table <<OrderDetails>> and time data from table <<Order>>,
    returns:
    - date in wich more pizzas were ordered.
    - pizza most ordered at this date.
    - quantity of orders for this pizza.
    """

    df_orders = pd.DataFrame(list(Order.objects.all().values()))

    if df_orders.empty:
        raise NoDataException("No data, impossible do generate statistic for most popular pizza")

    days_occurrances = df_orders["date"].value_counts().sort_values(ascending=False)
    most_popular_day = days_occurrances.index[0]

    df_most_popular_orders = df_orders.loc[df_orders["date"] == most_popular_day]
    df_most_popular_order_ids = list(df_most_popular_orders.id)

    df_order_details = pd.DataFrame(OrderDetails.objects.filter(id__in=df_most_popular_order_ids).values())

    pizza, quantity = get_most_ordered_pizza_and_quantity(df_order_details)

    return most_popular_day, pizza, quantity
