from django.shortcuts import render, get_object_or_404
from .models import Session

# Create your views here.

def training(request):
    """ A view to return the index page """

    sessions = Session.objects.all()

    context = {
        'sessions': sessions,
    }

    return render(request, 'training/training.html', context)


def session_detail(request, session_id):
    """ A view to return the session detail page and its contents """

    session = get_object_or_404(Session, pk=session_id)

    context = {
        'session': session,
    }

    return render(request, 'training/session_detail.html', context)

