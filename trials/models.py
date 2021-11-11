from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Trial(models.Model):
    date = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    time = models.DecimalField(max_digits=6, decimal_places=2)
    selected_players = models.ManyToManyField(User)   # checkbox Y/N for all auth users ? 

    def __str__(self):
        return self.name
