""" Defines URL patterns for users """
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # login page
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    
    #log out page
    path('logout/', views.logout_view, name='logout_view'),
    
    # registraion page
    path('register/', views.register, name='register')
]