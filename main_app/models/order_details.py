from django.db import models

from main_app.models.order import Order
from main_app.models.pizzas import Pizzas


class OrderDetails(models.Model):
    """
    Model to store details of a Pizza Order
    """

    class Meta:
        managed = True
        db_table = "'main_app'.'order_details'"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizzas, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, blank=True)
