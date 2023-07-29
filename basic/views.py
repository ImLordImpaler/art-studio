from django.shortcuts import render, redirect

from django.contrib.auth import authenticate , login , logout
from .models import * 

def indexview(request):
    post_type =PostType.objects.all()
    posts = Posts.objects.all()
    context = {
        'posts':posts,
        'post_type': post_type
    }
    return render(request , "index.html", context = context)
    # return HttpResponse("<h1>Hello World</h1>")



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        auth = authenticate(request , username=username , password = password)
        
        if auth:
            login(request , auth)
            return redirect('indexview')
        else:
            context = {
                'error_message': 'User Not Found. Please Try again', 
                
            }
            return render(request , 'error_message.html', context=context)
    return render(request , 'login_page.html')


def logoutview(request):
    logout(request)
    return redirect('indexview')