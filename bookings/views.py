from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm

# Create your views here.

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("my_bookings")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "bookings/my_bookings.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)