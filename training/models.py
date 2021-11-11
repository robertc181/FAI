from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Session(models.Model):
    day = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    time = models.DecimalField(max_digits=6, decimal_places=2)
    attendees = models.ManyToManyField(User)  # pick users in an Array from auth 
    # comments = models.TextField() form that allows players to comment on session


    def __str__(self):
        return self.name


class Comments(models.Model):
    comment = models.CharField(max_length=254)
    training_session = models.ManyToManyField(Session)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return self.user