from django.urls import path
from . import views
urlpatterns = [
    path('usrinfo/',views.User_detail),
    path('Roleinfo/',views.Role_detail), 
    path('contentinfo/',views.Content_detail), 
    path('Fileinfo/',views.File_detail), 
    path('classinfo/',views.Class_detail),
    path('usrcreate/',views.User_create) 
   ]