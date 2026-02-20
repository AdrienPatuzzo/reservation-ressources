from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource
from django.core.exceptions import ValidationError
from django.db.models import Q

# Create your models here.
# On efface pas la réservation, on change son statut.
# Une réservation = une ressource, un utilisateur, une période, un statut
class Booking(models.Model):
    STATUS_CHOICES = [
        ('CONFIRMED', 'Confirmée'),
        ('CANCELLED', 'Annulée'),
    ]

    # Une réservation concerne UNE ressource, une ressource peut avoir plusieurs réservations
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    #Une réservation appartient à UN utilisateur, un utilisateur peut faire plusieurs réservations
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #DateTimeField car dans le TP on parle de créneaux horaires.
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CONFIRMED')
    #rempli à la création
    created_at = models.DateTimeField(auto_now_add=True)
    # mis à jour à chaque modification
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resource} - {self.start_date}"

    def clean(self):
        # Vérifier que la date de fin est après la date de début
        if self.start_date >= self.end_date:
            raise ValidationError("La date de fin doit être après la date de début.")

        # Vérifier les conflits de réservation
        overlapping_bookings = Booking.objects.filter(
            resource=self.resource,
            status='CONFIRMED'
        ).filter(
            Q(start_date__lt=self.end_date) &
            Q(end_date__gt=self.start_date)
        )

        # Si on modifie une réservation existante, on l'exclut
        if self.pk:
            overlapping_bookings = overlapping_bookings.exclude(pk=self.pk)

        if overlapping_bookings.exists():
            raise ValidationError("Cette ressource est déjà réservée sur ce créneau.")
