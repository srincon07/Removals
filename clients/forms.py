from django import forms

from clients.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phoneNumber']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'input'})
        }


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class':'input', 'form':'contact-form'
        }
    ))
    contact_sender = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'input', 'form':'contact-form'
        }
    ))
    contact_phoneNumber = forms.CharField(max_length=10, required=False, widget=forms.TextInput(
        attrs={
            'class':'input', 'form':'contact-form'
        }))
    contact_message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'input', 'form':'contact-form'
        }))