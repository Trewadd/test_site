from django.contrib.auth.models import User
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'item', 'publish_date', 'image', 'author']

    def clean_author(self):
        self.cleaned_data['author']
        return User()

