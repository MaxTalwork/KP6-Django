from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (BlogPostListView, BlogPostCreateView, BlogPostDeleteView, BlogPostDetailView,
                         BlogPostUpdateView, blog_main)

app_name = BlogsConfig.name
urlpatterns = [
    path('blog', blog_main, name='blogpost_main_page'),
    path('blogpost_list/', BlogPostListView.as_view(), name='blogpost_list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post'),
    path('post/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete')
]
