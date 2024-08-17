from django.contrib import admin
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'publication')
    list_filter = ('publication',)
    search_fields = ('name', 'description')