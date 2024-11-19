from django.urls import path
from . import views

from . import views


urlpatterns = [path("", views.say_hello, name="hello"),
               path("privacy/", views.privacyPage, name="privacy"),
               path("home/", views.homePage, name="home"),
               path("registrationpage/", views.registration_page, name="registrationpage"),
               path("chatpage/", views.chatpage, name="chatpage"),
               path("postpage/", views.postpage, name="postpage"),
               path("profilepage/", views.profilepage, name="profilepage"),
               path("loginXpage/", views.login_page, name="loginpage"),]