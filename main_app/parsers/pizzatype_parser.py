import pandas as pd
from django.db.utils import IntegrityError
from loguru import logger

from main_app.models.pizza_type import PizzaType

# TODO: add python deque and pandas chunksize feature to improve performance


def fetch_pizza_type() -> None:
    """Read file 'pizza_types.csv' from system folder and parses data to database"""

    logger.info("Starting fetch_pizza_type")

    df = pd.read_csv("data/pizza_types.csv", encoding="unicode_escape")
    df.rename(columns={"pizza_type_id": "id"}, inplace=True)

    data_set = df.to_dict(orient="records")

    for pizza_type in data_set:
        try:
            PizzaType.objects.get_or_create(**pizza_type)
        except IntegrityError as error:
            logger.error(f"Pizza type {pizza_type['id']} unable to be created: {error}")

    logger.info("fetch_pizza_type finished")
