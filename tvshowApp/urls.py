
from django.urls import path
from . import views

urlpatterns = [
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:tvshow_id>', views.showinfo),
    path('shows', views.display),
    path('shows/<int:tvshow_id>/edit', views.edit),
    path('shows/<int:tvshow_id>/update', views.update),
    path('shows/<int:tvshow_id>/destroy', views.destroy),
    path('', views.index),
]
