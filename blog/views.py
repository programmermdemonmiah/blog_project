from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Blog, Category

def blog_list(request):
    posts = Blog.objects.filter(status='Published').order_by('-created_at')
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        posts = posts.filter(category__slug=selected_category)

    context = {
        'title': 'Blog',
        'posts': posts,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Blog.objects.filter(status='Published', category=category).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'title': f'{category.name} - Blog',
        'posts': posts,
        'categories': categories,
        'selected_category': category_slug,
        'current_category': category,
    }
    return render(request, 'blog/blog_list.html', context=context)

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status='Published')
    recent_posts = Blog.objects.filter(status='Published').exclude(pk=post.pk).order_by('-created_at')[:3]
    categories = Category.objects.all()
    context = {
        'title': post.title,
        'post': post,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/blog_detail.html', context=context)

def search(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    posts = Blog.objects.filter(status='Published')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(content__icontains=query)
        )

    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    posts = posts.order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'title': f'Search: {query}' if query else 'Search',
        'posts': posts,
        'query': query,
        'categories': categories,
        'selected_category': category_slug,
    }
    return render(request, 'blog/search.html', context=context)
