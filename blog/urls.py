from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/category/<slug:category_slug>/', views.blog_by_category, name='blog_by_category'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
]
