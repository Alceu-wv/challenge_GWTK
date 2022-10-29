import pandas as pd
from django.db.utils import IntegrityError
from loguru import logger

from main_app.models.pizzas import Pizzas

# TODO: add python deque and pandas chunksize feature to improve performance


def fetch_pizzas() -> None:
    """Read file 'pizzas.csv' from system folder and parses data to database"""

    logger.info("Starting fetch_pizza")

    df = pd.read_csv("data/pizzas.csv", encoding="unicode_escape")
    df.rename(columns={"pizza_id": "id"}, inplace=True)

    data_set = df.to_dict(orient="records")

    for pizza in data_set:
        try:
            Pizzas.objects.create(**pizza)
        except IntegrityError as error:
            logger.warning(f"Pizza {pizza['id']} unable to be created: {error}")

    logger.info("fetch_pizza finished")
