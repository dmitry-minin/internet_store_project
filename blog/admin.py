from django.contrib import admin
from blog.models import BlogPost, PostAuthor


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview_image', 'is_published', 'views', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at', 'updated_at')
    ordering = ('-updated_at',)


@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    ordering = ('name',)