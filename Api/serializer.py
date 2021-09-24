from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    # updated = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        fields = ['email', 'password','mobile','is_active','created','updated']
        read_only_field = ('is_active',)
        