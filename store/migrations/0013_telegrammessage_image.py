# Generated by Django 5.0.6 on 2024-05-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_telegrammessage_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegrammessage',
            name='image',
            field=models.ImageField(null=True, upload_to='products', verbose_name='Фото'),
        ),
    ]