# Generated by Django 5.0.13 on 2025-06-04 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_purchase_price_product_sell_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_desc',
        ),
    ]
