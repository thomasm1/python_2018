from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

def index(request):
  #1. return HttpResponse('Index this ...')
  #2. return render(request, 'posts/index.html', { 
  #2.    'title': 'Latest Posts'    })
  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts':posts
  }
  return render(request, 'posts/index.html', context)

def details(request, id): 

  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }
  return render(request, 'posts/details.html', context)

  
# CONTROLLER -- Details, load views, interact with models
# Create your views here.
