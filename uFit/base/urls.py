from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.welcomePage, name="hello"),
    path("privacy/", views.privacyPage, name="privacy"),
    path("home/", views.homePage, name="home"),
    path("registrationpage/", views.registration_page, name="registrationpage"),
    path("chatpage/", views.chatpage, name="chatpage"),
    path("postpage/", views.postpage, name="postpage"),
    path("home/profilepage/<str:pk>", views.profilepage, name="profilepage"),
    path("loginpage/", views.login_page, name="loginpage"),
    path("loginpage/", auth_views.LoginView.as_view(), name="loginpage"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("create-message/", views.create_message, name="create-message"),
    path(
        "stream-chat-messages/", views.stream_chat_messages, name="stream-chat-messages"
    ),
    path("lobby/", views.lobby, name="lobby"),
    path("update-post/<str:pk>", views.updatePost, name="updatepost"),
    path("update-post/<int:pk>/", views.updatePost, name="update-post"),
    path("search-posts/", views.search_posts, name="search-posts"),
    path("home/profilepage/<str:pk>", views.profilepage, name="profilepage"),
    path("update-profile/<int:pk>", views.update_profile, name="update-profile"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
