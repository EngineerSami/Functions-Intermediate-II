# login_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success, name='success'),
    path('logout/', views.logout_view, name='logout'),
]
