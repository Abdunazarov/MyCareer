from dataclasses import field
from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance





class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    role = serializers.CharField()
    password = serializers.CharField(min_length=6, write_only=True)
    password2 = serializers.CharField(write_only=True)


    def create(self, validated_data):
        password = validated_data['password']

        if not password == validated_data['password2']:
            raise serializers.ValidationError({'Error': 'Passwords must match'})

        instance = User.objects.create(
            email=validated_data['email'],
            role=validated_data['role']
        )
        instance.set_password(password)
        instance.save()
        return instance


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        # filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')


        return {
            'email': user.email,
            'tokens': user.tokens
        }


from .utils import Util
import string
import random

class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def send_code(self, request_data):
        try:
            user = User.objects.get(email=request_data['email'])
        except User.DoesNotExist:
            return serializers.ValidationError({'Error': 'This user is not registered'})

        
        code = ''.join(random.choices(string.ascii_letters, k=10))
        data = {
            'email_subject': 'Password Reset Code',
            'email_body': f'''<h2>Please enter the following 10-digit code in order to reset your password. Code: <h1 style="color: red">{code}</h1></h2>''',
            'to_email': request_data['email']
        }

        Util.send_email(data)
        return code
        


class ResetPasswordSerializer(serializers.Serializer):
    reset_code = serializers.CharField(max_length=10)
    new_password = serializers.CharField(min_length=6)
    new_password2 = serializers.CharField(min_length=6)

    def save(self, request_data, email, code):
        user = User.objects.get(email=email)
        new_password = request_data['new_password']
        new_password2 = request_data['new_password2']

        if not code == request_data['reset_code']:
            raise serializers.ValidationError({'Error': 'Reset code is not valid or incorrect'})

        if not new_password == new_password2:
            raise serializers.ValidationError({'Error': 'Passwords do not match '})
        

        
        user.set_password(new_password)
        user.save()
