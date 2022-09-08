from django.db import models

# Create your models here.
class TshirtSize(models.Model):
    size = models.CharField(max_length=4, verbose_name='T-shirt Size')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.size


class PantsSize(models.Model):
    size = models.CharField(max_length=4, verbose_name='Pants Size')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.size


class ShoesSize(models.Model):
    size = models.CharField(max_length=4, verbose_name='Shoes Size')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.size


class BloodType(models.Model):
    bloodType = models.CharField(max_length=3, verbose_name='Blood Type')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.bloodType


class Genre(models.Model):
    genre = models.CharField(max_length=10, verbose_name='Genre')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.genre


class Position(models.Model):
    """Position model
    
    Model to register positions in the organisation
    """

    name = models.CharField(max_length=50, verbose_name='Position Name')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Positions'
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.name


class Collaborator(models.Model):
    """Collaborator model
    
    Model to register people who work within the organisation
    """

    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Position')
    bloodType = models.ForeignKey(BloodType, on_delete=models.PROTECT, verbose_name='Blood Type')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='Genre')
    tshirtSize = models.ForeignKey(TshirtSize, on_delete=models.PROTECT, verbose_name='T-shirt Size')
    pantsSize = models.ForeignKey(PantsSize, on_delete=models.PROTECT, verbose_name='Pants Size')
    shoesSize = models.ForeignKey(ShoesSize, on_delete=models.PROTECT, verbose_name='Shoes Size')
    firstName = models.CharField(max_length=50, verbose_name='First Name')
    lastName = models.CharField(max_length=50, verbose_name='Last Name')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    phoneNumber = models.CharField(max_length=10, verbose_name='Phone Number')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Address')
    salary = models.IntegerField(default=0, verbose_name='Salary Rate')
    hInsuranceProvider = models.CharField(max_length=50, null=True, blank=True, verbose_name='Health Insurance Provider')
    hInsuranceNumber = models.CharField(max_length=50, null=True, blank=True, verbose_name='Health Insurance Number')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Collaborators'
        ordering = ('-created',)

    def __str__(self) -> str:
        fullName = self.firstName + ' ' + self.lastName
        return fullName