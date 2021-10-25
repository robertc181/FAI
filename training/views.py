from django.shortcuts import render
from .models import Session

# Create your views here.

def training(request):
    """ A view to return the index page """

    sessions = Session.objects.all()

    context = {
        'sessions': sessions,
    }

    return render(request, 'training/training.html', context)