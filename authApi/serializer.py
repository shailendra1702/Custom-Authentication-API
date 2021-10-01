from Api.serializer import UserSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from Api.models import User


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(
        required=True, write_only=True, max_length=128)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'mobile', 'created']

    def validate(self, attrs):
        email = attrs.get('email', '')
        mobile = attrs.get('mobile', '')

        if email.find('@') == -1:
            raise serializers.ValidationError('Email should contain @ in it')

        if len(mobile) != 10 or not mobile.isdigit():
            raise serializers.ValidationError(
                'Invalid phone number must contain 10 digits and should numeric digit [0-9]')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # user.save()
        return user
