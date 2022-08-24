# Django
from dataclasses import field
from django.forms import ModelForm

# Models
from .models import Furniture_type, Furniture_item

class FurnitureItemForm(ModelForm):
    class Meta:
        model = Furniture_item
        fields = ['type', 'name']

