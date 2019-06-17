from django.db import models


class Item(models.Model):
    asset_name = models.CharField(max_length=30)
    asset_class = models.CharField(max_length=30)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    sold_assets = models.BooleanField(default = False)

    # def __str__(self):
    #     return self.asset_name
class PlotItem(models.Model):
    x_value = models.DecimalField(max_digits=30, decimal_places=2)
    y_value = models.DecimalField(max_digits=30, decimal_places=2)

