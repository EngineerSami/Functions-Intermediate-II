from django.urls import path
from .views import home, result

urlpatterns = [
    path('', home, name='index'),
    path('result', result, name='result'),
]
