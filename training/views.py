from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Session, Comment
from .forms import CommentForm, SessionForm
from django.contrib import messages

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

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print('data is valid', request.POST)
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.session = session
            # Save the comment to the database
            new_comment.save()
    comment_form = CommentForm()
    comments = Comment.objects.filter(session=session)
    session.attendees_list = session.attendees.all()
    context = {
        'session': session,
        'comment_form': comment_form,
        'comments': comments
    }

    return render(request, 'training/session_detail.html', context)


def session_attend(request, session_id):
    """ A view to return the session detail page and its contents """

    session = get_object_or_404(Session, pk=session_id)
    comments = Comment.objects.filter(session=session)
    session.attendees.add(request.user)
    session.save()
    session.attendees_list = session.attendees.all()
    comment_form = CommentForm()
    context = {
        'session': session,
        'comment_form': comment_form,
        'comments': comments
    }
    messages.success(request, f'You are attending the {session.name} on {session.day}')
    return render(request, 'training/session_detail.html', context)


def session_unattend(request, session_id):
    """ A view to return the session detail page and its contents """

    session = get_object_or_404(Session, pk=session_id)
    session.attendees.remove(request.user)
    session.save()
    comments = Comment.objects.filter(session=session)
    comment_form = CommentForm()
    session.attendees_list = session.attendees.all()
    context = {
    
        'session': session,
        'comment_form': comment_form,
        'comments': comments
    }
    messages.info(request, f'You are not attending the {session.name} on {session.day}')
    return render(request, 'training/session_detail.html', context)


def post_detail(request, slug):
    template_name = 'training/session_detail.html'
    session = get_object_or_404(Session, slug=slug)
    comments = session.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.session = session
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'session': session,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def add_session(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            session = form.save()
            messages.success(request, 'Successfully added a session!')
            return redirect(reverse('session_detail', args=[session.id]))
        else:
            messages.error(request, 'Failed to add session. Please check the details and try again')
    else: 
        form = SessionForm()
    template = 'training/add_session.html'
    context = {
        'form': form,
    }

    return render(request, template, context)