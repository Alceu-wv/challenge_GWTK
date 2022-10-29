from django.forms.models import model_to_dict
from drf_spectacular.utils import extend_schema
from loguru import logger
from rest_framework import viewsets
from rest_framework.response import Response

from main_app.exceptions import NoDataException
from main_app.statistics_generator.most_popular_pizza import get_most_popular_pizza
from main_app.statistics_generator.most_popular_pizza_day import get_most_popular_pizza_day


class StatisticsViewSet(viewsets.ViewSet):

    authentication_classes = []

    @extend_schema(
        summary="get most popular pizza",
        description="Returns information about the more ordered pizza according to all data",
    )
    def get_most_popular_pizza(self, request, *args, **kwargs):
        logger.info("Request for 'get_most_popular_pizza'")

        try:
            pizza, quantity = get_most_popular_pizza()

            result = {
                "pizza": model_to_dict(pizza),
                "quantity": quantity,
            }

        except NoDataException as error:
            logger.error(error)
            return Response({"detail": error.args[0]}, status=200)

        except Exception as error:
            response = {"detail": "Unknown error trying to get most popular pizza"}
            logger.error(error)
            return Response(response, status=500)

        return Response(result, status=200)

    @extend_schema(
        summary="get most popular pizza and day",
        description="Returns information about the more ordered pizza on the day the most pizzas were sold",
    )
    def get_most_popular_pizza_day(self, request, *args, **kwargs):
        logger.info("Request for 'get_most_popular_pizza_day'")

        try:

            most_popular_day, pizza, quantity = get_most_popular_pizza_day()

            result = {
                "most_popular_day": {
                    "day": most_popular_day,
                    "pizza": model_to_dict(pizza),
                    "quantity": quantity,
                }
            }

        except NoDataException as error:
            logger.error(error)
            return Response({"detail": error.args[0]}, status=200)

        except Exception as error:
            response = {"detail": "Unknown error trying to get most popular pizza and day"}
            logger.error(error)
            return Response(response, status=500)

        return Response(result, status=200)

    @extend_schema(
        summary="get most sold pizzas",
        description="Returns sorted list of the most sold pizza types",
    )
    def get_most_sold_pizzas(self, request, *args, **kwargs):
        logger.info("Request for 'get_most_sold_pizzas'")

        # TODO:

        return Response({"detail": "not implemented, please hire me for more"}, status=501)

    @extend_schema(
        summary="get most popular pizza ingredients",
        description="Returns what are the most wanted ingredients",
    )
    def get_most_popular_pizza_ingredients(self, *arg, **kwargs):
        logger.info("Request for 'get_most_popular_pizza_ingredients'")

        # TODO:

        return Response({"detail": "not implemented, please hire me for more"}, status=501)
