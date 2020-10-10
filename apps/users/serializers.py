from django.contrib.auth import authenticate
from rest_framework import serializers
from apps.users.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    """Serializer to validate user"""
    email = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email'].lower()).exists():
            raise serializers.ValidationError("You are already signed up. Please Login.")
        attrs['email'] = attrs['email'].lower()
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user_obj = User.objects.create(**validated_data)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        if not User.objects.filter(email=attrs['email'].lower()).exists():
            raise serializers.ValidationError("Invalid Email")
        user_obj = authenticate(email=attrs['email'].lower(), password=attrs['password'])
        if not user_obj:
            raise serializers.ValidationError("Invalid credentials")
        attrs['user'] = user_obj
        return attrs

class UserSerializer(serializers.ModelSerializer):
    """Serializer to serialize user"""
    class Meta:
        model = User
        fields = ('id','email', 'username')
