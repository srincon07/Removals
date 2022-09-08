# Django
from django.contrib import admin

# Models
from .models import Collaborator, Position, BloodType, ShoesSize, PantsSize, TshirtSize, Genre

# Register your models here.
@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'position', 'phoneNumber', 'salary')

admin.site.register(Position,)
admin.site.register(BloodType,)
admin.site.register(ShoesSize,)
admin.site.register(PantsSize,)
admin.site.register(TshirtSize,)
admin.site.register(Genre,)