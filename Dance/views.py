from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import ApplicationSerializer
from .models import Application
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(request_body=ApplicationSerializer)
class CreateApplicationAPI(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer