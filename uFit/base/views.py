from django.shortcuts import render


# Create your views here.
def say_hello(request):
    return render(request, "base/index.html", {})

def home(request):
    return render(request, 'home.html')

def chatpage(request):
    return render(request, 'chatpage.html')