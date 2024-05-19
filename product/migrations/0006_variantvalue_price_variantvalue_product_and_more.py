# Generated by Django 5.0.6 on 2024-05-15 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_product_variant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantvalue',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='variantvalue',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product', verbose_name='Продукт'),
        ),
        migrations.DeleteModel(
            name='ProductVariant',
        ),
    ]