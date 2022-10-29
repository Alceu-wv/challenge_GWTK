from collections import deque

import pandas as pd
from django.db.utils import IntegrityError
from loguru import logger

from main_app.models.order import Order

# TODO: add pandas chunksize feature to improve performance


def fetch_order() -> None:
    """Read file 'orders.csv' from system folder and parses data to database"""

    logger.info("Starting fetch_order")

    df = pd.read_csv("data/orders.csv", encoding="unicode_escape")
    df.rename(columns={"order_id": "id"}, inplace=True)
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["time"] = pd.to_datetime(df["time"], format="%H:%M:%S")

    data_set = deque(df.to_dict(orient="records"))

    for order in data_set:
        try:
            Order.objects.create(**order)
            logger.debug(order["id"])
        except IntegrityError as error:
            logger.warning(f"Order {order['id']} unable to be created: {error}")

    logger.info("fetch_order finished")
