from django.urls import path
from . import views

urlpatterns = [
    path('', views.trials, name='trials'),
    path('<trial_id>', views.trial_detail, name='trial_detail'),
    
]