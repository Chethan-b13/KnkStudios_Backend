from django.shortcuts import render
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from .serializers import ApplicationSerializer,PostSerializer
from .models import Application, Post
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(request_body=ApplicationSerializer)
class CreateApplicationAPI(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

@swagger_auto_schema(request_body=PostSerializer)
class PostDetailsAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):

        if self.request.method == "GET":
            return (permissions.AllowAny,)
        elif self.request.method in ["PUT","DELETE","PATCH"]:
            return (permissions.IsAuthenticated,)
        return []

@swagger_auto_schema(request_body=PostSerializer)
class CreatePostAPI(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer

