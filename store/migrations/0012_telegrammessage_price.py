# Generated by Django 5.0.6 on 2024-05-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_telegrammessage_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrammessage',
            name='price',
            field=models.FloatField(default=None, null=True, verbose_name='Цена'),
        ),
    ]