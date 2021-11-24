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



class Comment(models.Model):
    session = models.ForeignKey(Session,on_delete=models.CASCADE,related_name ='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)