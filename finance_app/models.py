from django.db import models


class Item(models.Model):
    asset_name = models.CharField(max_length=30)
    asset_class = models.CharField(max_length=30)
    asset_quantity = models.CharField(max_length=30)
    asset_price = models.DecimalField(max_digits=9, decimal_places=2)
    sold_assets = models.BooleanField(default = False)

    def __str__(self):
        return self.asset_name


