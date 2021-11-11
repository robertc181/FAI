from django.shortcuts import render, get_object_or_404
from .models import Trial

# Create your views here.


def trials(request):
    trials = Trial.objects.all()

    for trial in trials:
        trial.player_selected = request.user in trial.selected_players.all()

    context = {
        'trials': trials,
    }

    return render(request, 'trials/trials.html', context)


def trial_detail(request, trial_id):
    """ A view to return the session detail page and its contents """

    trial = get_object_or_404(Trial, pk=trial_id)

    context = {
        'trial': trial,
    }

    return render(request, 'trials/trial_details.html', context)

