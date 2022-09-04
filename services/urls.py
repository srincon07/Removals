from django.urls import path

# Views
from . import views

urlpatterns = [
    path(
        route='',
        view=views.booking_service,
        name='index',
    ),
    path(
        route='services/',
        view=views.ServicesAllView.as_view(),
        name='services',
    ),
]