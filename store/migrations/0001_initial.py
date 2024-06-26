# Generated by Django 5.0.6 on 2024-05-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='Логотип')),
                ('name', models.CharField(max_length=255, verbose_name='Название магазина')),
                ('shortInfo', models.CharField(max_length=455, verbose_name='Краткое описание')),
                ('location', models.CharField(max_length=255, verbose_name='Адресс')),
                ('owner', models.CharField(max_length=255, verbose_name='ФИО владельца')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон номер')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]
