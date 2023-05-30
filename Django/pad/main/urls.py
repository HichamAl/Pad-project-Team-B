from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path("profile/", views.profile, name="profile"),
path("", views.home, name="home"),
path("challenges/", views.challenges, name="challenges"),
path("challenges-1/", views.challenges1, name="challenges-1"),
path("credit/", views.credit, name="credit"),
path("leaderboard/", views.leaderboard, name="leaderboard"),
path('avatar/', include('avatar.urls')),
path("challenges-2/", views.challenges2, name="challenges-2"),
path("challenges-3/", views.challenges3, name="challenges-3"),
path("challenges-4/", views.challenges4, name="challenges-4"),
path("combinations/", views.combinations, name="combinations"),
] 

#Allows profile pictures to be uploaded
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
