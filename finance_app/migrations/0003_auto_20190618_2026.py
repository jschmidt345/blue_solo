# Generated by Django 2.2.2 on 2019-06-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0002_item_value_sum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='value_sum',
            new_name='value_sum_current',
        ),
        migrations.AddField(
            model_name='item',
            name='value_sum_sold',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
