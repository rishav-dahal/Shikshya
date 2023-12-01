from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['u_id', 'role_id' ,'u_name' ,'u_email']
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['role_id', 'role']
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['role_id', 'role']