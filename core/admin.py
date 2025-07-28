from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Permisos extra', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']
