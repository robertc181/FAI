from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('<session_id>', views.session_detail, name='session_detail'),
    path('attend/<session_id>', views.session_attend, name='session_attend'),
]