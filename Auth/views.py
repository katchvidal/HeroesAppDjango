from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from .form import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.

class Registro( generic.CreateView):
    model=User
    form_class=RegisterForm
    template_name = '05-Auth/registro.html'
    success_url= reverse_lazy('Login')


class LoginView( LoginView ):
    template_name='05-Auth/login.html'
    