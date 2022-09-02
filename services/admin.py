# Django
from django.contrib import admin

# Models
from .models import Service, Move_type, Service_type, Service_item, Service_status

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('clientId', 'pickUp', 'dropOff')


class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('service', 'item', 'quantity')


class ServiceStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Move_type)
admin.site.register(Service_type)
admin.site.register(Service_item, ServiceItemAdmin)
admin.site.register(Service_status, ServiceStatusAdmin)