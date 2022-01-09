from django.contrib import admin
from .models import Item, ItemDetail, Photo
# Register your models here.

admin.site.register(Item)
admin.site.register(ItemDetail)
admin.site.register(Photo)
