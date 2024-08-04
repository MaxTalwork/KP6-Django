from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.models import BlogPost


def blog_main(request):
    return render(request, 'blogs/blogpost_main_page.html')


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ("title", "description", "preview", "publication")
    success_url = reverse_lazy('blogs:blogpost_list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)



class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "description", "preview", "publication")
    success_url = reverse_lazy('blogs:blogpost_list')

    def get_success_url(self):
        return reverse('blogs:post', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogs:blogpost_list')
