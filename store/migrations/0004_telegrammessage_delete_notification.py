# Generated by Django 5.0.6 on 2024-05-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_notification_chat_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('chat_id', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
