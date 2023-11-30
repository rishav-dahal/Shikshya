from rest_framework import serializers
class UserSerializer(serializers.Serializer):
    u_id = serializers.IntegerField
    role_id = serializers.IntegerField()
    u_name = serializers.CharField(max_length=10)
    u_email =serializers.EmailField()
    hash = serializers.CharField(max_length=100)
    verification = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField()
    

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