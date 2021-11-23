from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('<session_id>', views.session_detail, name='session_detail'),
    path('attend/<session_id>', views.session_attend, name='session_attend'),
    path('unattend/<session_id>', views.session_unattend, name='session_unattend'),
    path('add/', views.add_session, name='add_session'),
    path('delete/<int:session_id>', views.delete_session, name='delete_session'),
    path('edit/<int:session_id>', views.edit_session, name='edit_session'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]
