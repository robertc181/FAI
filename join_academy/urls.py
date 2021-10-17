from django.urls import path
from . import views

urlpatterns = [
    path('', views.join_academy, name='join_academy')
]