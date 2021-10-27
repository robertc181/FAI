from django.shortcuts import render

# Create your views here.

def myprofile(request):
    """ A view to return the profile page """

    return render(request, 'myprofile/profile.html')