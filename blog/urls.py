from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.blog_detail, name = 'blog_detail'),
    path('new/', views.blog_create, name = 'blog_new'),
    path('delete/<int:pk>/', views.blog_delete, name = 'blog_delete'),
    path('update/<int:pk>/', views.blog_update, name = 'blog_update'),
]