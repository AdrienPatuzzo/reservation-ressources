from django.urls import path
from .views import BookingCreateView, MyBookingsView
from . import views

urlpatterns = [
    path("create/", BookingCreateView.as_view(), name="booking_create"),
    path("my/", MyBookingsView.as_view(), name="my_bookings"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
