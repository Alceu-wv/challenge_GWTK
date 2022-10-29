from django.db import models


class Order(models.Model):
    """
    Model to store Pizza orders
    """

    class Meta:
        managed = True
        db_table = "'main_app'.'order'"

    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
