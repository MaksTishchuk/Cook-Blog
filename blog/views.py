from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    """View для постов"""

    model = Post

    def get_queryset(self):
        return Post.objects.select_related('category').filter(
            category__slug=self.kwargs.get('slug')
        )


class PostDetailView(DetailView):
    """View для открытия конкретного поста"""

    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

