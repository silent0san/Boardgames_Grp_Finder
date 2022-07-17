from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_meeting', views.add_meeting, name='add-meeting'),
]
