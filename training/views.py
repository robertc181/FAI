from django.shortcuts import render

# Create your views here.

def training(request):
    """ A view to return the index page """

    return render(request, 'training/training.html')