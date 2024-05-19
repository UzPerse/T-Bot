from django.contrib import admin
import admin_thumbnails
from .models import *


@admin_thumbnails.thumbnail('image')
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortInfo', 'owner', 'phone', 'image_tag']


admin.site.register(Store, StoreAdmin)