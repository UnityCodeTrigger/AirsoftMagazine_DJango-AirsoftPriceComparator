from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('register/', views.userRegister, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),

    path('ver_usuarios/', views.ver_usuarios, name='ver_usuarios'),
]