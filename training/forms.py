from django import forms
from .models import Comment, Session


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
