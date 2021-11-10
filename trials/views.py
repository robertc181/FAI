from django.shortcuts import render
from .models import Trial

# Create your views here.


def trials(request):
    trials = Trial.objects.all()

    context = {
        'trials': trials,
    }

    return render(request, 'trials/trials.html', context)