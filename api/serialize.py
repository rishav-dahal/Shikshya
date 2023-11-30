from rest_framework import serializers
from . models import *

class UserSerializer(serializers.Serializer):
    role_id = serializers.IntegerField()
    u_name = serializers.CharField(max_length=10)
    u_email =serializers.EmailField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

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

        

    
