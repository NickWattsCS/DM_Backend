from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import DanceUser

class CustomUserAdmin(UserAdmin):
    model = settings.AUTH_USER_MODEL
    list_display = ['email']

admin.site.register(DanceUser, CustomUserAdmin)
# Register your models here.
