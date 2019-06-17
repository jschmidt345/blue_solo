# Generated by Django 2.2.2 on 2019-06-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0006_auto_20190617_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='sold_assets',
            field=models.CharField(max_length=30),
        ),
    ]
