from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm


class HomeView(ListView):
    """View для главной страницы"""

    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().select_related('category', 'author').prefetch_related(
            'comment').order_by('-id')


class PostListView(ListView):
    """View для постов"""

    model = Post
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs.get('slug')
        ).select_related('category', 'author').prefetch_related('comment').order_by('-id')


class PostDetailView(DetailView):
    """View для открытия конкретного поста"""

    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

    def get_queryset(self):
        slug = self.kwargs.get('post_slug', '')
        q = super().get_queryset()
        return q.filter(slug=slug).select_related('category', 'author').prefetch_related('comment')


class CreateComment(CreateView):
    """View для создания комментария"""

    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()