from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('films/', views.films, name='films'),
    path('films/<int:film_id>/', views.film_detail, name='film_detail'),
    path('actors/', views.actors, name='actors'),
]