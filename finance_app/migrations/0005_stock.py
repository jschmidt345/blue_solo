# Generated by Django 2.2.2 on 2019-06-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_app', '0004_item_port_return'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock1', models.CharField(max_length=30)),
                ('stock2', models.CharField(max_length=30)),
                ('stock3', models.CharField(max_length=39)),
            ],
        ),
    ]