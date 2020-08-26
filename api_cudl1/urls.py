"""api_cudl1 URL Configuration

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
from django.urls import path, include
from web.views import (GetAllPostAPIView, create_post, save_newpost, email_view, save_email, new_post, list_post, delete_post, edit_post, savepost)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', GetAllPostAPIView.as_view()),
    path('posts/<int:pk>/', GetAllPostAPIView.as_view()),
    path('posts/update/<int:pk>/', GetAllPostAPIView.put, name="update"),
    path('create_post', create_post, name='create'),
    path('new_post', new_post, name='new_post'),
    path('save/', save_newpost, name='save'),#test POSTMAN
    path('email/', email_view, name='email'),
    path('process', save_email, name='pro'),
    path('list_post', list_post, name='list'),
    path('delete/(?P<pk>\d+)/$', delete_post, name='delete_post'),
    path('edit/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    path('savepost', savepost, name='savepost'),
]
