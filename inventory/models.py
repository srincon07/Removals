from django.db import models

# Create your models here.
class Furniture_type(models.Model):
    """Inventory types Model
    
    Model to register types of inventory Eg, White furniture, Dinning etc.
    """

    name = models.CharField(max_length=50, verbose_name='Name')
    comment = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Furniture Types'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Furniture_item(models.Model):
    """Furniture items model
    
    Model to register items related to inventory types.
    """

    type = models.ForeignKey(Furniture_type, on_delete=models.PROTECT, verbose_name='Type')
    name = models.CharField(max_length=50, verbose_name='Furniture name')
    active = models.BooleanField(default=True, verbose_name='Active')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Items'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name