from django.urls import path
from .views import *

urlpatterns = [
    path('add-application',CreateApplicationAPI.as_view(),name='add-application'),
    path('create-post',CreatePostAPI.as_view(),name='create-post'),
    path('post/<slug:slug>',PostDetailsAPI.as_view(),name='get-update-posts')
]