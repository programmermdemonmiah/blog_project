from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'blog_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def blog_count(self, obj):
        return obj.blogs.count()
    blog_count.short_description = 'Blogs'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('show_image', 'title', 'category', 'status', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'short_description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

    def show_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="60" height="60" '
                f'style="object-fit:cover;border-radius:4px;" />'
            )
        return mark_safe('<span style="color:#999">No Image</span>')
    show_image.short_description = 'Image'
