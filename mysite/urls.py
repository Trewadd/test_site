from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from blog.core import views as core_views
from blog import views as b_views
from registration import views as r_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('registration/', include('registration.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
