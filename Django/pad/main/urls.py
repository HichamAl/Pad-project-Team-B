from django.urls import path
from . import views

urlpatterns = [
path("profile/", views.profile, name="profile"),
path("home/", views.home, name="home"),
path("index/", views.index, name="index"),
path("enter/", views.enter, name="enter"),
path("challenges/", views.challenges, name="challenges"),
path("challenges-1/", views.challenges1, name="challenges-1"),
]