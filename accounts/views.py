from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import permissions
from django.db.utils import DatabaseError
from .serializers import *
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=SignupSerializer)
    def post(self,request,format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        try:

            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'Error':"User with Email Already Exist"},status=500)
                else:
                    if len(password) < 6 :
                        return Response({'Error':"Password Length should be greater than 6"},status=500)
                    else:
                        user = User.objects.create_user(email=email,name=name,password=password)
                        user.save()
                        return Response({'Success':"User Created SuccessFully"})
            else:
                return Response({'Error':"Passwords do not match"},status=500)
        except DatabaseError as ex:
            return Response({'Error':"User with Email Already Exist"},status=500)


class MakeAdmin(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    @swagger_auto_schema(request_body=makeAdminSerializer)
    def post(self,request):
        data = request.data
        email = data['email']
        try:
            if self.request.user.is_superuser:
                user = User.objects.get(email=email)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                return Response({'SUCCESS','User was made as Admin'})
            else:
                return Response({'FORBIDDEN','You Have to be an  Admin'})
        except Exception as e:
            print(e)
            return Response({"ERROR","User with Email Doesn't Exists"})
        

class UserDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        profile = Profile.objects.get(user=request.user)
        
        user_details = {
            'uid': profile.user.id,
            'email': profile.user.email,
            'name': profile.user.name,
            'is_superuser': profile.user.is_superuser,
            'avatar': profile.avatar,
            'bio': profile.bio,
            'style': profile.style,
            'team': profile.team,
            'slug': profile.slug,
        }
        return Response(user_details)
    
    @swagger_auto_schema(request_body=ProfileSerializer)
    def put(self,request):
        data = request.data
        profile = Profile.objects.get(user=request.user)
        for key in data.keys():
            setattr(profile, key, data[key])

        profile.save()
        return Response(model_to_dict(profile))

