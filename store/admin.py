from django.contrib import admin
import admin_thumbnails
from .utils import send_message_to_telegram
from .models import *
from .models import TelegramMessage

@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


@admin_thumbnails.thumbnail('image')
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortInfo', 'owner', 'phone', 'image_tag']


admin.site.register(Store, StoreAdmin)
