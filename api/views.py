from django.shortcuts import render
from . models import *
from .serialize import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from json.decoder import JSONDecodeError
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

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
            print("Request Body:", request.body)
            python_data = JSONParser().parse(request)
            print("Parsed Data:", python_data)
            serializer = UserSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                return Response ( {'Success':'True'})
            return Response(serializer.errors)
        except JSONDecodeError as e:
            error_message = f'JSON parse error - {str(e)}'
            return Response({'error': error_message})
            


