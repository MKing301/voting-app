from django.urls import path
from . import views

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('poll/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/results/', views.poll_results, name='poll_results'),
]