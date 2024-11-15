from django.urls import path
from . import views


urlpatterns = [
    path("", views.welcomePage, name="welcome"),
    path("privacy/", views.privacyPage, name="privacy"),
]
