from django.urls import path
from .views import *

urlpatterns = [
    path('signup',SignupView.as_view(),name='signup'),
    path('makeAdmin',MakeAdmin.as_view(),name='makeAdmin'),
    path('user_details',UserDetails.as_view(),name='user-details'),
    path('update_user',UserDetails.as_view(),name='update-user-details'),
]