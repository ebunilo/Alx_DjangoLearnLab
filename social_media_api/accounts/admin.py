from django.contrib import admin

from .models import CustomUser, Profile

class ProfileAdmin(admin.ModelAdmin):
    """Profile Administration"""
    list_display = ('user', 'bio', 'phone', 'picture')


class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Administration"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
