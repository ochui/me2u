from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'phone_number_status',  'country']
    list_editable = ['phone_number_status']
    list_filter = ['date_joined', 'last_login', 'is_active', 'is_staff']
    model = CustomUser
