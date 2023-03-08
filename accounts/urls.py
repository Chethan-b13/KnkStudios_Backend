from django.urls import path
from .views import *

urlpatterns = [
    path('signup',SignupView.as_view(),name='signup'),
    path('makeAdmin',MakeAdmin.as_view(),name='makeAdmin')
]