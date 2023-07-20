from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['Username', 'Email', 'Password']

