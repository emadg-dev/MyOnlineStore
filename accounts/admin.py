from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserAddForm, UserChangeForm

class CustomUserAdmin(UserAdmin): 
    add_form = UserAddForm 
    form = UserChangeForm 
    model = CustomUser
    list_display = ['username','email','city','supplier']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('city',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('city',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('supplier',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('supplier',)}),
    )

    
admin.site.register(CustomUser, CustomUserAdmin)
