from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as baseUserAdmin
# Register your models here.

class UserAdmin(baseUserAdmin):
    list_display = ['full_name','email',]
    list_display_links = ['full_name','email',]

    fieldsets = (  
        ("Personal info", {"fields": ("full_name","email",'password')}), 
    )

    ordering = []



admin.site.register(User,UserAdmin)