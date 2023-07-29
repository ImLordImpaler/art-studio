from django.shortcuts import render, redirect
from django.http import HttpResponse
from basic.models import * 


def add_post(request):
    posts = Posts.objects.all() 
    post_types = PostType.objects.all()
    print(request.FILES)
    if request.method == "POST":
        painting_name = request.POST.get('painting_name')
        
        painting_pic = request.FILES.get('painting_pic')
        post_type = request.POST.get('post_type')
        post_type = PostType.objects.filter(name = post_type).values('id')
        post_type_obj = post_type[0].get('id')
        
        Posts.objects.create(post_type_id = post_type_obj , name = painting_name , image = painting_pic)
         
        
    context = {
        'posts': posts,
        'post_types': post_types
    }
    return redirect('admin_page')

def delete_post(request , pk):
    posts = Posts.objects.filter(id = pk)
    if not posts.exists():
        return HttpResponse("<h1>No Post Found</h1>")
    posts.delete()
    return redirect('admin_page')

def admin_page(request):
    posts = Posts.objects.all() 
    post_types = PostType.objects.all()
    print(post_types)
    context = {
        'posts': posts,
        'post_types': post_types
    }
    return render(request , 'adminpage.html', context=context)


def add_post_type(request):
    if request.method == 'POST':
        new_type = request.POST.get('painting_type')
        
        PostType.objects.create(name = new_type)
        
        return redirect('admin_page')
    
def delete_post_type(request, pk):
    
    post_type = PostType.objects.filter(id =pk).values('id')
    if not post_type:
        return HttpResponse('<h1>No Post Type. Please Contact Rachit Saxena</h1>')
    PostType.objects.filter(id =pk).delete()
    return redirect('admin_page')