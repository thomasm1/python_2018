from django.shortcuts import render
from django.http import HttpResponse
# CONTROLLER -- Details, load views, interact with models
# Create your views here.

def index(request):
  #return HttpResponse('Index this ...')
  return render(request, 'posts/index.html')