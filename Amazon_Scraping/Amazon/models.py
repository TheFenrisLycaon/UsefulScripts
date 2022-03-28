from django.db import models


class Amazon(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    name = models.TextField(db_column="Name", blank=True, null=True)
    # Field name made lowercase.
    reviews = models.BigIntegerField(db_column="Reviews", blank=True, null=True)
    # Field name made lowercase.
    price = models.BigIntegerField(db_column="Price", blank=True, null=True)
    # Field name made lowercase.
    savings = models.TextField(db_column="Savings", blank=True, null=True)
    # Field name made lowercase.
    delivery = models.TextField(db_column="Delivery", blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    free_option = models.TextField(db_column="Free Option", blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    more_option = models.TextField(db_column="More Option", blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    more_prices = models.TextField(db_column="More Prices", blank=True, null=True)
    # Field name made lowercase.
    special = models.TextField(db_column="Special", blank=True, null=True)
