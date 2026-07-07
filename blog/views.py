from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Blog

def blog_list(request):
    posts = Blog.objects.filter(status='Published').order_by('-created_at')
    context = {
        'title': 'Blog',
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status='Published')
    recent_posts = Blog.objects.filter(status='Published').exclude(pk=post.pk).order_by('-created_at')[:3]
    context = {
        'title': post.title,
        'post': post,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/blog_detail.html', context=context)

def search(request):
    query = request.GET.get('q', '')
    posts = Blog.objects.none()
    if query:
        posts = Blog.objects.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query),
            status='Published'
        ).order_by('-created_at')
    context = {
        'title': f'Search: {query}' if query else 'Search',
        'posts': posts,
        'query': query,
    }
    return render(request, 'blog/search.html', context=context)
