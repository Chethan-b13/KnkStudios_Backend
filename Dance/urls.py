from django.urls import path
from .views import *

urlpatterns = [
    path('add-application',CreateApplicationAPI.as_view(),name='add-application'),
]