from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def get_home(request):
    """ A view to return the index page """

    if not User.objects.filter(is_superuser=True).first():
        user = User.objects.create(
            username='admin',
            email='admin@mywebsite.com',
            is_superuser=True,
        )
        user.set_password('some password')
        user.save()
        print(user.username)

    return render(request, 'home/index.html')
