from django.views import generic
from datetime import datetime
from django.shortcuts import redirect
from .models import Post
from registration.views import send_mail
from django.urls import reverse
from django.conf import settings
import re


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'latest_posts_list'
    paginate_by = 10

    def post(self, request):
        send_mail(request)
        return redirect(reverse('home'))

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=datetime.now()).order_by('-create_date')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    current_post = int()

    def get_queryset(self):
    #     # image = request.FILES['image_file'].file.read()
    #     # Post.objects.create(image=image)
    #     # import boto3
    #     # queryset = Post.objects.filter(pk=self.kwargs['pk'])
    #     # for i in queryset:
    #     #     print('this is:',i)
    #     # print(queryset)
    #     # s3 = boto3.client('s3')
    #     # s3.download_file(settings.AWS_STORAGE_BUCKET_NAME, 'OBJECT_NAME', 'FILE_NAME')
    #     queryset =
        # print(queryset)
        return  Post.objects.filter(pk=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        pk = re.search("[0-9]+", str(request.get_full_path)).group()
        send_mail(request)
        return redirect(reverse('post', args=(pk,)))


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # print('context', context)
    #     posts = Post.objects.all()
    #     print(posts)
    #     context['posts'] = posts
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cars'] = Car.objects.all()
    #     return context

    # def image(request):
    #     image_file = request.FILES['image_file'].file.read()
    #     Post.objects.create(image=image_file)


