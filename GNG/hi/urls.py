from django.urls import path
from hi import views

urlpatterns = [
    path('', views.index),
    path('play_again', views.play_again),
]