from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

'''posts=[
    {'id':1, 'title':'how to do tricep extensions', 'body':'this is an explanation of how to do tricep extensions', 'host':'John Doe'},
    {'id':2, 'title':'how to do bicep curls', 'body':'this is an explanation of how to do bicep curls', 'host':'John Doe'},
    {'id':3, 'title':'how to squat' , 'body':'this is an explanation of how to do squats', 'host':'John Doe'},
] '''

post=[
    {'id':1, 'title':'how to do tricep extensions', 'body':'this is an explanation of how to do tricep extensions', 'host':'John Doe'}
]

# Create your views here.
def say_hello(request):
    return render(request, "base/index.html", {})

def privacyPage(request):
    return render(request, 'base/privacy.html')

def homePage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'base/home.html', context)

def registration_page(request):
    return render(request, 'base/registration_page.html')

def chatpage(request):
    return render(request, 'base/chatpage.html')

def postpage(request):
    return render(request, 'base/postpage.html', {'post':post}) 

def profilepage(request):
    return render(request, 'base/profilepage.html')

def login_page(request):
    return render(request, 'base/login_page.html')

def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance = post)


    context = {}
    return render(request, 'base/post_form.html', context)