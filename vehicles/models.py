from django.db import models

# Create your models here.
class Shift(models.Model):
    """Shift model
    
    Model to record shifts for the vehicle's availability
    """

    start_time = models.TimeField(verbose_name='Start Time')
    end_time = models.TimeField(verbose_name='End Time')
    date = models.DateField(verbose_name='Shift Date')
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Shifts'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.start_time + ' ' + self.end_time

class Vehicle(models.Model):
    """Vehicles model
    
    Model to register all the vehicles that deliver the service
    """

    registration = models.CharField(max_length=10, verbose_name='Registration')
    brand = models.CharField(max_length=50, verbose_name='Brand')
    model = models.CharField(max_length=50, verbose_name='Model')
    year = models.CharField(max_length=4, verbose_name='Year')
    capacity = models.IntegerField(verbose_name='Capacity')
    registration_due = models.DateField(null=True, blank=True, verbose_name='Registration Due Date')
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Vehicles'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.registration