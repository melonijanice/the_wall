from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('wall',views.wall),
    path('post_message',views.post_message),
    path('post_comment',views.post_comment),
    path('delete_message',views.delete_message)
    
]