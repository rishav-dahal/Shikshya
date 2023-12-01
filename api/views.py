from django.shortcuts import render
from . models import *
from .serialize import *
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from json.decoder import JSONDecodeError
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

@api_view(['GET'])
def User_detail(request):
    usr=User.objects.all()
    serilizer =UserSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json')

def Role_detail(request):
    usr=Role.objects.all()
    serilizer =RoleSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json')

def Content_detail(request):
    usr=Content.objects.all()
    serilizer =ContentSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json')

def File_detail(request):
    usr=File.objects.all()
    serilizer =FileSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json')

def Class_detail(request):
    usr=Class.objects.all()
    serilizer =ClassSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json')

@csrf_exempt
@api_view(['POST'])
def User_create(request):
    if request.method == 'POST' :
        try:
            python_data = JSONParser().parse(request)
            serializer = UserRegistrationSerilizer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response ( {'Success':'True'})
            return Response(serializer.errors)
        except JSONDecodeError as e:
            error_message = f'JSON parse error - {str(e)}'
            return Response({'error': error_message})
        

# @api_view(['POST'])
#

# def User_Login(request):
    
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         validated_data = serializer.validated_data
#         return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def User_Registration(self, request):
#     serializer = UserRegistrationSearilizer(data=request.data)
#     if serializer.is_valid():
#         return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

