from django.contrib import admin
from .models import L1_Name, Issue_History, Alarm, CustomUser

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(L1_Name)
admin.site.register(Issue_History)
admin.site.register(Alarm)

