from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='entries', blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    item = models.CharField(max_length=1000)
    create_date = models.DateTimeField('create date', auto_now_add=True)
    publish_date = models.DateTimeField('publish date', blank=False)
    update_date = models.DateTimeField('last update date', blank=True, auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.item



