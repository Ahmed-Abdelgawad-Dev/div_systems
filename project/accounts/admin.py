from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('first_name', 'last_name',
                    'country_code', 'phone_number', 'gender', 'birthdate', 'is_admin', 'avatar', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('first_name', 'password')}),
        ('Personal info', {'fields': (
            'country_code', 'phone_number', 'gender', 'birthdate', 'avatar', 'email',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'country_code', 'phone_number', 'gender', 'birthdate', 'avatar', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
# Unregister as we use our custom user model
admin.site.unregister(Group)
