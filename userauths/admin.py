from django.contrib import admin
from .models import CustomUser, Profile

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
admin.site.register(CustomUser, CustomUserAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
    search_fields = ('user__username', 'first_name', 'last_name', 'email')
    list_filter = ('state_of_origin', 'nationality')
admin.site.register(Profile)