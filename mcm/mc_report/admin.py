from django.contrib import admin
from .models import L1_Name, Issue_History, Alarm, CustomUser
<<<<<<< HEAD
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# admin.site.register(CustomUser, CustomUserAdmin)
=======

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
admin.site.register(CustomUser, CustomUserAdmin)
>>>>>>> 63237a4161cd1471be41e140154dcb2f15bb5f6d
admin.site.register(L1_Name)
admin.site.register(Issue_History)
admin.site.register(Alarm)

