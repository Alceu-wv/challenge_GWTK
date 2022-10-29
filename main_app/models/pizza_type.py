from django.db import models


class PizzaType(models.Model):
    """
    Model to store types os Pizza
    """

    class Meta:
        managed = True
        db_table = "'main_app'.'pizza_type'"

    id = models.CharField(primary_key=True, max_length=31, editable=False)
    name = models.CharField(max_length=123, null=True, blank=True)
    category = models.CharField(max_length=63, null=True, blank=True)
    ingredients = models.CharField(max_length=511, null=True, blank=True)
