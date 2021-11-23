from django.urls import path
from . import views

urlpatterns = [
    path('', views.trials, name='trials'),
    path('<trial_id>', views.trial_detail, name='trial_detail'),
    path('add/', views.add_trial, name='add_trial'),
    path('edit/<int:trial_id>', views.edit_trial, name='edit_trial'),
    path('delete/<int:trial_id>', views.delete_trial, name='delete_trial'),
    
]