from rest_framework import serializers
from . models import *
import re
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate

class UserSerializer(serializers.Serializer):
    role_id = serializers.IntegerField()
    u_name = serializers.CharField(max_length=10)
    u_email =serializers.EmailField()
    password =serializers.CharField(write_only=True)
        
class RoleSerializer(serializers.Serializer):
    role_id = serializers.IntegerField()
    role_name = serializers.CharField()

class ContentSerializer(serializers.Serializer):
    content_id = serializers.IntegerField()
    content = serializers.CharField()
    file_id = serializers.CharField()
    created_at = serializers.DateTimeField
    u_id = serializers.IntegerField
    class_id = serializers.IntegerField
    title = serializers.CharField
    
class FileSerializer(serializers.Serializer):
    file_id = serializers.CharField
    path = serializers.CharField
    u_id = serializers.IntegerField
    class_id = serializers.IntegerField
 
class ClassSerializer(serializers.Serializer):
    class_id = serializers.IntegerField
    subject_name = serializers.CharField
    semester = serializers.IntegerField

class UserRegistrationSerilizer(serializers.Serializer):
    u_email =serializers.EmailField(validators=[EmailValidator()])
    password =serializers.CharField(write_only=True)
    role_id = serializers.IntegerField()
    u_name = serializers.CharField(max_length=10)

    def validate_email(self, value):
        # Custom validation for email uniqueness
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email address is already in use.')
        return value

    def validate_password(self, value):
        # Custom validation for password strength 
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        
         # Check for at least one uppercase letter
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter.')

        # Check for at least one lowercase letter
        if not any(char.islower() for char in value):
            raise serializers.ValidationError('Password must contain at least one lowercase letter.')

        # Check for at least one digit
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit.')

        # Check for at least one special character 
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError('Password must contain at least one special character.')

        return value
    def create(self, validated_data):
        # User.set_password('secure_password')
        User.save
        return User.objects.create(**validated_data)
    
# class UserLoginSerializer(serializers.Serializer):
#     u_email = serializers.EmailField()
#     password = serializers.CharField()
#     print("hello world"),
#     def validate(self,data):
#         u_email = data.get('u_email')
#         password = data.get('password')

#         # Authenticate user
#         user = authenticate(u_email=u_email, password=password)

#         if user and user.is_active:
#             data['u_email'] = user
#             return data
#         else:
#             raise serializers.ValidationError('Invalid credentials')

        

    
