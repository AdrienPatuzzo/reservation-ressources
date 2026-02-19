from django.db import models

# Create your models here.
# Une catégorie permet de regrouper les ressources.
class Category(models.Model):
    name = models.CharField(max_length=100)

# Important pour l'admin Django, permet de rendre l'affichage lisible
    def __str__(self):
        return self.name

# Même logique que pour catégorie, une localisation peut représenter batiment / salle / entrepot / etc...
class Location(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

# limite des valeurs possibles, première valeur sotckée en base, deuxième valeur affichée a l'utilisateur.
class Resource(models.Model):
    RESOURCE_TYPES = [
        ('ROOM', 'Salle'),
        ('EQUIPMENT', 'Équipement'),
    ]

    #Nom de la ressource
    name = models.CharField(max_length=150)
    #Doit être >= longeur de l'equipement, Impose le menu déroulant
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    #Une ressource appartient à UNE catégorie, une catégorie peut avoir plusieurs ressources, si la catégorie est supprimée, ses ressources aussi
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
