from django.urls import path
from hi import views

urlpatterns = [
    path('', views.gng),
    path('destroy_session', views.destroy_session),
]