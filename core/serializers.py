from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name')

class UserObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserObj
        fields = ('id','text_data',)