# Generated by Django 5.0.6 on 2024-05-21 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_telegrammessage_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegrammessage',
            name='image',
        ),
    ]
