# Generated by Django 3.2.16 on 2024-12-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_workshops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderNumber',
            field=models.PositiveIntegerField(unique=True, verbose_name='Номер заказа'),
        ),
    ]
