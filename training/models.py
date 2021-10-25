from django.db import models

# Create your models here.

class Session(models.Model):
    day = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    time = models.DecimalField(max_digits=6, decimal_places=2)
    attendees =  models.CharField(max_length=254)

    def __str__(self):
        return self.name