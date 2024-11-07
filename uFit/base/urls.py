from django.urls import path
from . import views

urlpatterns = [path("", views.say_hello, name="hello")]

urlpatterns = [path("", views.home, name="home")]
urlpatterns = [path("", views.chatpage, name="chatpage")]