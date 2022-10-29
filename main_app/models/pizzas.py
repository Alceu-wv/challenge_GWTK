from django.db import models

from main_app.models.pizza_type import PizzaType


class Pizzas(models.Model):
    """
    Model to store Pizza data
    """

    class Meta:
        managed = True
        db_table = "'main_app'.'pizzas'"

    SIZE_CHOICES = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )

    id = models.CharField(primary_key=True, max_length=31, editable=False)
    pizza_type = models.ForeignKey(PizzaType, on_delete=models.SET_NULL, null=True)
    size = models.CharField(choices=SIZE_CHOICES, max_length=3, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
