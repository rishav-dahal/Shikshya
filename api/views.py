from django.shortcuts import render
from . models import *
from .serialize import *
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from json.decoder import JSONDecodeError
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from api import UserLoginSerializer
from rest_framework.views import APIView
from .models import File

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
        

@api_view(['POST'])
def Save_audio(self,request):
    audio_file = request.FILES.get('audioFile')
    if audio_file:
        # Save the audio file
        fs = FileSystemStorage(location='media/audio')  # Adjust the location to your desired path
        filename = fs.save(audio_file.name, audio_file)
        return JsonResponse({'message': 'Audio file uploaded successfully', 'filename': filename})
    else:
        return JsonResponse({'error': 'No audio file received'}, status=400)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSearilizer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

