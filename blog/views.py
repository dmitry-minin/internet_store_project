from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BlogPostWithAuthorForm
from blog.models import BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-updated_at')


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'].views += 1
        context['object'].save()
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostWithAuthorForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostWithAuthorForm
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:home')
