from django.db import models


class Item(models.Model):
    asset_name = models.CharField(max_length=30)
    asset_class = models.CharField(max_length=30)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    sold_assets = models.BooleanField(default=False)
    returns = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    value_sum_current = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    value_sum_sold = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    port_return = models.DecimalField(max_digits=10,  decimal_places=2, default=0)





