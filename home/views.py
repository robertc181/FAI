from django.shortcuts import render

# Create your views here.

def get_home(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')