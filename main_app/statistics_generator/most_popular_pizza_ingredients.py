import pandas as pd

from main_app.exceptions import NoDataException
from main_app.models import OrderDetails
from main_app.statistics_generator.helpers import get_popularity_rank


# TODO: not implemented
def get_most_popular_pizza_ingredients():
    """
    Returns a ranking of the most popular ingredients based on
    how many pizzas have sold and their ingredients compile
    which ingredients are most popular.
    """

    order_details = pd.DataFrame(list(OrderDetails.objects.all().values()))

    if order_details.empty:
        raise NoDataException("No data, impossible do generate statistic for most popular pizza")

    pizza_rank = get_popularity_rank(order_details)

    pass
