from django.shortcuts import render
from . models import *
from .serialize import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def User_detail(request):
    usr=User.objects.all()
    serilizer =UserSerializer(usr,many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')

def Role_detail(request):
    usr=Role.objects.all()
    serilizer =RoleSerializer(usr,many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')

def Content_detail(request):
    usr=Content.objects.all()
    serilizer =ContentSerializer(usr,many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')

def File_detail(request):
    usr=File.objects.all()
    serilizer =FileSerializer(usr,many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')

def Class_detail(request):
    usr=Class.objects.all()
    serilizer =ClassSerializer(usr,many=True)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type='application/json')





