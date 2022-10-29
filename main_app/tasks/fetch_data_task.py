from celery import shared_task
from loguru import logger

from main_app.parsers import fetch_order, fetch_order_details, fetch_pizza_type, fetch_pizzas


@shared_task(bind=True, name="fetch_data_task")
def fetch_data_task(self):
    """
    Celery task to fetch data from root folder 'data' to system database.

    Brings data into four database tables and their filenames:
    - <<PizzaType>> _ 'data/pizza_types.csv'
    - <<Pizzas>> _ 'data/pizzas.csv'
    - <<Order>> _ 'data/orders.csv'
    - <<OrderDetails>> _ 'data/order_details.csv'

    IMPORTANT: Do not change the functions execution sequence!!!
    """

    try:
        logger.info("Sarting fetch_data_task")

        fetch_pizza_type()
        fetch_pizzas()
        fetch_order()
        fetch_order_details()

        logger.info("fetch_data_task finished")
    except Exception as error:
        logger.error(f"Error fetching data {error}")
