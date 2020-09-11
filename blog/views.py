from django.views import generic
from datetime import datetime
from django.shortcuts import redirect
from .models import Post
from registration.views import send_mail
from django.urls import reverse
import re


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'latest_posts_list'
    paginate_by = 10

    def post(self, request):
        send_mail(request)
        return redirect(reverse('blog:home'))

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=datetime.now()).order_by('-create_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    current_post = int()

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = re.search("[0-9]+", str(request.get_full_path)).group()
        send_mail(request)
        return redirect(reverse('blog:post', args=(pk,)))
