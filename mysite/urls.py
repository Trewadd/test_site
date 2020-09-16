from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# from blog.core import views as core_views
# from blog import views as b_views
# from  import views as r_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('registration/', include('registration.urls')),

    # path('', b_views.IndexView.as_view(), name='home'),
    # path('post/<int:pk>', b_views.DetailView.as_view(), name='post'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
