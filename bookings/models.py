from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource

# Create your models here.
#On efface pas la réservation, on change son statut.
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