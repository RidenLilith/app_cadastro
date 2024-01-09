from django.urls import path
from app_cadastro_filmes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies, name='movies'),
    path('events/', views.events, name='events'),
    path('persons/', views.persons, name='persons'),
    path('events/editions/', views.editions, name='editions'),
    path('persons/ditectors/', views.directors, name='directors'),
    path('persons/roteirists/', views.roteirists, name='roteirists'),
    path('persons/actors/', views.actors, name='actors'),
    path('movies/info/', views.info, name='info')
]
