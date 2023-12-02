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
from rest_framework.views import APIView
from .models import File
from openai import OpenAI
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import os

@api_view(['GET'])
def User_detail(request):
    usr=User.objects.all()
    serilizer =UserSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json', status=status.HTTP_200_OK)
    
@api_view(['GET'])
def Role_detail(request):
    usr=Role.objects.all()
    serilizer =RoleSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json', status=status.HTTP_200_OK)

def Content_detail(request):
    usr=Content.objects.all()
    serilizer =ContentSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json', status=status.HTTP_200_OK)

def File_detail(request):
    usr=File.objects.all()
    serilizer =FileSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json', status=status.HTTP_200_OK)

def Class_detail(request):
    usr=Class.objects.all()
    serilizer =ClassSerializer(usr,many=True)
    return Response(serilizer.data,content_type='application/json', status=status.HTTP_200_OK)

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
        

@api_view(['POST'])

# def User_Login(request):
#     python_data = JSONParser().parse(request)
#     serializer = UserLoginSerializer(data=request.data)
#     if serializer.is_valid():
#         validated_data = serializer.validated_data
#         return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Save_audio(self,request):
    client = OpenAI(api_key='api_key')  #keepapi key 
    audio_file = request.FILES.get('audioFile')
    if audio_file:
        # Save the audio file
        fs = FileSystemStorage(location='media/audio')
        filename = fs.save(audio_file.name, audio_file)
        store_file(self,request,filename)
        transcript = client.audio.translations.create(
            model="whisper-1", 
            file=audio_file
        )

        summarize = transcript.text

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": "Please give the summary of this online class in json format, and 'title', 'summary', 'topics_dicussed','point_to_remember' in json format make sure to give topics_discussed and point_to_remember in text only in 50 words"},
                {"role": "user", "content": summarize}
            ]
        )
        try:
            serializer = FileSerializer(data=response)
            if serializer.is_valid():
                serializer.save()
                return Response ( {'Success':'True'})
            return Response(serializer.errors)
        except JSONDecodeError as e:
            error_message = f'JSON parse error - {str(e)}'
            return Response({'error': error_message})
        

def store_file (self,request, filename):
    serializer=FileSerializer(data=request.data)
    if serializer.is_valid():
        return Response({'message': 'audio file saved in database'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def home(request):
    return render (request,"base.html")



# def User_Registration(self, request):
#     serializer = UserRegistrationSearilizer(data=request.data)
#     if serializer.is_valid():
#         return Response({'message': 'Registration successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
