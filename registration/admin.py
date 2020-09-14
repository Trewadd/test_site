from django.contrib import admin

from .models import UserProfile
from .forms import UserForm

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('user',  'logged')


admin.site.register(UserProfile, UserAdmin)
