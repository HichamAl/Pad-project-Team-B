from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("profile/", views.profile, name="profile"),
path("home/", views.home, name="home"),
path("", views.index, name="index"),
path("enter/", views.enter, name="enter"),
path("challenges/", views.challenges, name="challenges"),
path("challenges-1/", views.challenges1, name="challenges-1"),
path("credit/", views.credit, name="credit"),
path("leaderboard/", views.leaderboard, name="leaderboard"),
path('avatar/', include('avatar.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
