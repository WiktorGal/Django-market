from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('singup/', views.singup, name='singup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
]
