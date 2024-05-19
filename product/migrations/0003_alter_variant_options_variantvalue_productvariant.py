# Generated by Django 5.0.6 on 2024-05-14 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'verbose_name': 'Названия варианта', 'verbose_name_plural': 'Варианты название'},
        ),
        migrations.CreateModel(
            name='VariantValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение варианты')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.variant', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Значение варианты',
                'verbose_name_plural': 'Значение варианты',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Цена')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product', verbose_name='Продукт')),
                ('variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.variantvalue', verbose_name='Варианты')),
            ],
            options={
                'verbose_name': 'Вариант продукта',
                'verbose_name_plural': 'Варианты продукты',
            },
        ),
    ]