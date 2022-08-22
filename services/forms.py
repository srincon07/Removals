# Django
from django import forms
from django.forms import ModelForm

# Services Models
from .models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['pickUp', 'pickUpComment','dropOff', 'dropOffComment', 'date', 'move', 'type']
        widgets = {
            'pickUp': forms.TextInput(attrs={'class': 'input'}),
            'pickUpComment': forms.Textarea(attrs={'class': 'input', 'rows': '2'}),
            'dropOff': forms.TextInput(attrs={'class': 'input'}),
            'dropOffComment': forms.Textarea(attrs={'class': 'input', 'rows': '2'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'move': forms.Select(attrs={'class': 'input'}),
            'type': forms.RadioSelect(),
        }