from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Trial
from .forms import TrialForm
from django.contrib import messages

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


def add_trial(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TrialForm(request.POST, request.FILES)
        if form.is_valid():
            trial = form.save()
            messages.success(request, 'Successfully added a trial!')
            return redirect(reverse('trial_detail', args=[trial.id]))
        else:
            messages.error(request, 'Failed to add trial. Please check the details and try again')
    else: 
        form = TrialForm()
    template = 'trials/add_trial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_trial(request, trial_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that')
        return redirect(reverse('home'))

    trial = get_object_or_404(Trial, pk=trial_id)
    trial.delete()
    messages.success(request, 'trial deleted')
    return redirect(reverse('trials'))


def edit_trial(request, trial_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that')
        return redirect(reverse('home'))

    trial = get_object_or_404(Trial, pk=trial_id)
    if request.method == 'POST':
        form = TrialForm(request.POST, request.FILES, instance=trial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the trial!')
            return redirect(reverse('trial_detail', args=[trial.id]))
        else:
            messages.error(request, 'Failed to update the trial. Please check the details and try again')
    else:
        form = TrialForm(instance=trial)
        messages.info(request, 'You are editing this trial')

    template = 'trials/edit_trial.html'
    context = {
        'form': form,
        'trial': trial,
    }

    return render(request, template, context)
