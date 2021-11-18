from django.shortcuts import render

# Create your views here.

def join_academy(request):
    """ A view to return the index page """

    return render(request, 'join_academy/join_academy.html')

