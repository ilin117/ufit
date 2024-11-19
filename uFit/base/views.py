from django.shortcuts import render


# Create your views here.
def welcomePage(request):
    return render(request, "base/welcome.html", {})


def privacyPage(request):
    return render(request, "base/privacy.html")
    return render(request, "base/privacy.html")


def homePage(request):
    return render(request, "base/home.html")


def registration_page(request):
    return render(request, "base/registrationpage.html")


def chatpage(request):
    return render(request, "base/chatpage.html")


def postpage(request):
    return render(request, "base/postpage.html")


def profilepage(request):
    return render(request, "base/profilepage.html")


def login_page(request):
    return render(request, "base/loginpage.html")
