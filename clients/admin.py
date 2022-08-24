# Django
from django.contrib import admin

# Models
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phoneNumber')

admin.site.register(Client, ClientAdmin)