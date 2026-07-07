from django.shortcuts import render
from blog.models import Blog

def index(request):
    posts = Blog.objects.filter(status='Published').order_by('-created_at')
    context = {
        'title': "Home",
        'posts': posts,
    }
    return render(request, 'home/index.html', context=context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})