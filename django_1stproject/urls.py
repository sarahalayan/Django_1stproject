"""
URL configuration for django_1stproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('', include("blog.urls")),
    path('login',
         auth_views.LoginView.as_view(template_name='users/login.html'), 
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
           name='logout'),
    path('profile/',user_views.profile, name='profile'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
           name='password_reset'),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
           name='password_reset_complete'),
   
]
"""
password-reset-confirm: This is the URL endpoint or path that indicates the password reset confirmation view. It's usually associated with a Django view that handles the confirmation of the password reset.

<uidb64>: This is a URL-safe base64-encoded user ID. It's used to identify the user who requested the password reset. The actual user ID is encoded in base64 to ensure URL safety.

<token>: This is a unique token associated with the password reset request. It's included in the URL to verify the authenticity of the password reset request and prevent unauthorized users from resetting passwords.
"""
 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
