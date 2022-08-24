from django.urls import path

# Views
from . import views

urlpatterns = [
    path(
        route='',
        view=views.booking_service,
        name='index',
    ),
]