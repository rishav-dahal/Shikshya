from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['u_id', 'role_id' ,'u_name' ,'u_email']
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['role_id', 'role']
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display=['file_id', 'file']
    
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display=['content_id', 'content_json','file','created_at']
    
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=['class_id', 'subject_name','semister']