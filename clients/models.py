from django.db import models

# Create your models here.

class Client(models.Model):
    """Client model
    
    Model to record all the subscribed clients
    """
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=50, verbose_name='Email')
    phoneNumber = models.CharField(max_length=20, verbose_name='Phone Number')
    cardNumber = models.CharField(max_length=20, null=True, blank=True, verbose_name='Card Number')
    cardName = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name on Card')
    cardExp = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Clients'
        ordering = ('-created',)

    def __str__(self) -> str:
        """Return client name"""
        return self.name