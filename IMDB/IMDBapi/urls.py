from django.urls import path
from . import views

urlpatterns = [
    path("imdb/all/", views.home, name="home0"),
    path("imdb/<str:res>/", views.home, name="home"),
    path("imdb/search/<str:q>/", views.search, name="search"),
]