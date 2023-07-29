from django.shortcuts import render

from django.http import HttpResponse
from .models import * 

def indexview(request):
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return render(request , "index.html", context = context)
    # return HttpResponse("<h1>Hello World</h1>")

