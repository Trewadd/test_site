from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View
from .tokens import account_token
from .forms import UserForm
from .models import UserProfile
from .emails import send_mail


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def registration(request):
    registered = False
    if request.method == 'POST' and 'registration' in request.POST:
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        send_mail(request)
        user_form = UserForm()
    return render(request, 'registration/registration.html',
                          {'user_form': user_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST' and request:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your account was inactive.')
        else:
            print('Someone tried to login and failed.')
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login")
    else:
        return render(request, 'registration/login.html', {})


class AccountView(View):
    def get(self, request, uidb64, token):
        try:
            uidb = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uidb)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_token.check_token(user, token):
            login(request, user)
            prof_obj = UserProfile.objects.filter(user=uidb).values_list('user', 'logged')
            UserProfile.objects.filter(user_id=prof_obj[0][0]).update(logged=prof_obj[0][1] + 1)
            return redirect(reverse('home'))
        else:
            return render(request, 'registration/invalid.html')
