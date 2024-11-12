from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='dojo_list'),
    path('create_dojo', views.create_dojo, name='create_dojo'),
    path('create_ninja', views.create_ninja, name='create_ninja'),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo, name='delete_dojo'),
]
