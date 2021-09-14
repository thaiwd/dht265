from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


def index(request):
    object_list = Course.objects.all()
    return render(request, 'home/home.html', {'objects': object_list, 'nav': 'home'})


def about(request):
    return render(request, 'home/introduce.html', {'nav': 'about'})
