from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username', 'email']
    add_fieldsets = (
        (None, {
            "fields": (
                'email', 'username', 'password1', 'password2',      
            ),
        }),
    )
    fieldsets = (
        (None, {
            "fields": (
                'username', 'password', 'about', 'email', 'first_name', 'last_name', 'age', 'experience_in_years',
            ),
        }),
    )
    
    

admin.site.register(CustomUser, CustomUserAdmin)