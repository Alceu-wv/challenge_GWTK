from collections import deque

import pandas as pd
from django.db.utils import IntegrityError
from loguru import logger

from main_app.models.order_details import OrderDetails

# TODO: add pandas chunksize feature to improve performance


def fetch_order_details() -> None:
    """Read file 'order_details.csv' from system folder and parses data to database"""

    logger.info("Starting fetch_order_details")

    df = pd.read_csv("data/order_details.csv", encoding="unicode_escape")
    df.rename(columns={"order_details_id": "id"}, inplace=True)

    data_set = deque(df.to_dict(orient="records"))

    for order_details in data_set:
        try:
            OrderDetails.objects.get_or_create(**order_details)
        except IntegrityError as error:
            logger.warning(f"OrderDetails {order_details['id']} unable to be created: {error}")

    logger.info("fetch_order_details finished")
