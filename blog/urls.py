from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    BlogPostListView,
    BlogPostCreateView,
    BlogPostDeleteView,
    BlogPostDetailView,
    BlogPostUpdateView,
    blog_main,
)

app_name = BlogConfig.name
urlpatterns = [
    path("blogpost_list/", BlogPostListView.as_view(), name="blogpost_list"),
    path("post/<int:pk>/", BlogPostDetailView.as_view(), name="post"),
    path("blogpost_create/", BlogPostCreateView.as_view(), name="blogpost_create"),
    path("blogpost_update/<int:pk>/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("blogpost_delete/<int:pk>/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
]
