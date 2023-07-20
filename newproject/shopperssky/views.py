from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

@api_view(['POST'])
def register(request):
    user = Register.objects.all()
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    Password = request.data.get('Password')
    Username = request.data.get('Username')
    Email = request.data.get('Email')
    try:
        if Username :
            user = Register.objects.get(Username=Username, Password=Password)
        else:
            user = Register.objects.get(Email=Email, Password=Password)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response ({'WELCOME TO SHOPPERSSKY'})
    except:
        return Response({'invalid credentials'})
