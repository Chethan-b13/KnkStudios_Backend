from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.utils import DatabaseError


# Create your views here.
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        try:

            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'Error':"User with Email Already Exist"})
                else:
                    if len(password) < 6 :
                        return Response({'Error':"Password Length should be greater than 6"})
                    else:
                        user = User.objects.create_user(email=email,name=name,password=password)
                        user.save()
                        return Response({'Success':"User Created SuccessFully"})
            else:
                return Response({'Error':"Passwords do not match"})
        except DatabaseError as ex:
            return Response({'Error':"User with Email Already Exist"})