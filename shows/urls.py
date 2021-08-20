from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/createshow', views.createshow),
    path('shows/<int>', views.view),
    path('shows/delete/<show_id>', views.delete),
    path('shows/<int>/edit', views.edit),
    path('shows/<show_id>/editshow', views.editshow),

]
