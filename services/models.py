# Django
from django.db import models

# Clients
from clients.models import Client

# Vehicles
from vehicles.models import Vehicle

# Inventory
from inventory.models import Furniture_item

# Create your models here.
class Move_type(models.Model):
    """Move type model
    
    Model to record the types of offered services 
    """

    name = models.CharField(max_length=255, verbose_name='Move type')
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Move types'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Service_type(models.Model):
    """Service type model
    
    Model to register type of offered services.
    """

    name = models.CharField(max_length=50, verbose_name='Service Type')
    condition = models.TextField(null=True, blank=True, verbose_name='Service Type Conditiions')
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Service Types'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Service_status(models.Model):
    """Service status model
    
    Model to register the status for the services.
    """

    name = models.CharField(max_length=50, default='Booked', verbose_name='Service Status')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Service Status'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    """Service model
    
    Model to record all the requested removal services
    """
    
    clientId = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name='Client')
    move = models.ForeignKey(Move_type, on_delete=models.PROTECT, verbose_name='Move type')
    type = models.ForeignKey(Service_type, on_delete=models.PROTECT, verbose_name='Service type')
    status = models.ForeignKey(Service_status, on_delete=models.PROTECT, default=1, verbose_name='Service Status')
    vehicle = models.ManyToManyField(Vehicle, related_name='vehicles', verbose_name='Vehicle')
    furniture_item = models.ManyToManyField(Furniture_item, related_name='furniture_items', through='Service_item', verbose_name='Furniture Item')
    pickUp = models.CharField(max_length=100, verbose_name='Pick-up')
    pickUpComment = models.TextField(null=True, blank=True, verbose_name='Pick-up Comments')
    dropOff = models.CharField(max_length=100, verbose_name='Drop-off')
    dropOffComment = models.TextField(null=True, blank=True, verbose_name='Drop-off Comments')
    date = models.DateField(verbose_name='Moving Date')
    comment = models.TextField(blank=True, null=True, verbose_name='Service Comments')
    price = models.IntegerField(verbose_name='Service Price', null=True)
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('-created',)

    def __str__(self) -> str:
        return str(self.clientId)



class Service_item(models.Model):
    """Service item model
    
    Model to register items and its quantity provided by the customer
    """

    item = models.ForeignKey(Furniture_item, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    quantity = models.IntegerField(verbose_name='Qty', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Service Items'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.item
