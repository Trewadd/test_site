from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Post
from .forms import PostForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'publish_date', 'image')

    #For save post group users
    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
