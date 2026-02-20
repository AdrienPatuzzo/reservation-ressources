from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Sécurité : seul le propriétaire ou un admin peut annuler
    if booking.user != request.user and not request.user.groups.filter(name="ADMIN").exists():
        messages.error(request, "Vous n'avez pas le droit d'annuler cette réservation.")
        return redirect("my_bookings")

    if booking.status == "CANCELLED":
        messages.warning(request, "Cette réservation est déjà annulée.")
        return redirect("my_bookings")

    booking.status = "CANCELLED"
    booking.save()

    messages.success(request, "Réservation annulée avec succès.")
    return redirect("my_bookings")