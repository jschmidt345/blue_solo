from django.db import models


class Item(models.Model):
    asset_name = models.CharField(max_length=30)
    asset_class = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    sold_assets = models.BooleanField(default = False)

    # def __str__(self):
    #     return self.asset_name


