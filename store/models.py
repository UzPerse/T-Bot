from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
import admin_thumbnails
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import send_message_to_telegram


# Stores model
class Store(models.Model):
    image = models.ImageField(verbose_name="Логотип", upload_to='logo', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Название магазина")
    shortInfo = models.CharField(max_length=455, verbose_name="Краткое описание")
    location = models.CharField(max_length=255, verbose_name="Адресс")
    owner = models.CharField(max_length=255, verbose_name="ФИО владельца")
    phone = models.CharField(max_length=255, verbose_name="Телефон номер")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name

    def image_tag(self):
        return format_html('<img src="{}" style="width:70px; height:70px"/>'.format(self.image.url))
    

# Message Model
class TelegramMessage(models.Model):
    title = models.CharField(max_length=455, verbose_name="Название продукта")
    description = models.TextField(blank=True, verbose_name="Краткое описание")
    price = models.FloatField(default=None, null=True, blank=False, verbose_name="Цена продукта")
    image = models.URLField(max_length = 200, verbose_name="Фото URL")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        message = f'{self.title}\n\n{self.description}\n\nPrice: {self.price}$'
        image_url = self.image
        send_message_to_telegram(message, image_url)

    
    class Meta:
        verbose_name = "Телеграм оповещение"
        verbose_name_plural = "Телеграм оповещения"

    def __str__(self):
        return self.title
    
