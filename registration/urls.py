from django.urls import path
from . import views

app_name = 'registration'
urlpatterns=[
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('link_login/<slug:uidb64>/<slug:token>/', views.AccountView.as_view(), name='send_mail'),
    path('logout/', views.user_logout, name='logout'),
]