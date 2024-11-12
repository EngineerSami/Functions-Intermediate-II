from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Redirects to /shows
    path('shows', views.all_shows, name='all_shows'),  # Display all shows
    path('shows/new', views.new_show, name='new_show'),  # Form to add a new show
    path('shows/create', views.create_show, name='create_show'),  # Process form to create new show
    path('shows/<int:id>', views.show_details, name='show_details'),  # Display details of a show
    path('shows/<int:id>/edit', views.edit_show, name='edit_show'),  # Form to edit show
    path('shows/<int:id>/update', views.update_show, name='update_show'),  # Process update form
    path('shows/<int:id>/destroy', views.delete_show, name='delete_show'),  # Delete a show
]
