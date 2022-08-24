# Django
from django.contrib import admin

# Models
from .models import Furniture_type, Furniture_item

# Register your models here.
class FurnitureItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')

admin.site.register(Furniture_type)
admin.site.register(Furniture_item, FurnitureItemAdmin)