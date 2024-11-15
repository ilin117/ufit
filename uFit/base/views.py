from django.shortcuts import render


# Create your views here.
def welcomePage(request):
    return render(request, "base/welcome.html", {})


def privacyPage(request):
    return render(request, "base/privacy.html")
