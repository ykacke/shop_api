from . import models
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField(min_length=8)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def validate_username(self, username):
        try:
            User.objects.filter(username=username).exists()
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError("Username already exists")

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(min_length=8)

class SMSCodeSerializer(serializers.Serializer):
    sms_code = serializers.CharField(min_length=8)