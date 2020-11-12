from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def index(request):
    posts= Blog.objects.all()
    return render(request,"blog/index.html",{"posts":posts})

def blogPost(request,id):
    blogji = Blog.objects.filter(post_id=id)[0]
    print(blogji)
    return render(request,"blog/blogPost.html",{"blogji":blogji})