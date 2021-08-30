"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from .views import Registro, LoginView

#LogOut 
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LogoutView


#   Password Reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro', Registro.as_view(), name="Registro" ),
    path('accounts/login/', LoginView.as_view(), name="Login" ),
    path('logout', LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name='LogOut'),

    #   Vistas Necesarias para Recuperar Password
    path('reset_password', auth_views.PasswordResetView.as_view( template_name='05-Auth/password_reset.html'), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view( template_name='05-Auth/password_reset_sent.html' ), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(  template_name='05-Auth/password_reset_form.html' ), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view( template_name='05-Auth/password_reset_done.html'), name="password_reset_complete"),

]