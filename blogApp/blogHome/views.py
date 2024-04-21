from django.shortcuts import render,HttpResponse
from .models import Blog

# Create your views here.


def home(request):
    
    blog = Blog.objects.all()

    context = {

        "blog" : blog
    }

    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contacts.html")

def content(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        "blog":blog
    }
    return render (request,"blogContents.html",context)


def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")