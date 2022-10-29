from typing import Tuple

import numpy as np
import pandas as pd

from main_app.exceptions import NoDataException
from main_app.models import OrderDetails, Pizzas
from main_app.statistics_generator.helpers import get_most_ordered_pizza_and_quantity


def get_most_popular_pizza() -> Tuple[Pizzas, np.int64]:

    """Query all elements from table <<OrderDetails>> to get most ordered pizza and how many times was it ordered"""

    df_order_details = pd.DataFrame(list(OrderDetails.objects.all().values()))

    if df_order_details.empty:
        raise NoDataException("No data, impossible do generate statistic for most popular pizza")

    pizza, quantity = get_most_ordered_pizza_and_quantity(df_order_details)

    return pizza, quantity
