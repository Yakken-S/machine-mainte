from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from allauth.account.forms import SignupForm

class CustomUserCreationForm(SignupForm):
    username = forms.CharField(max_length=12, required=True, label="従業員番号")

    class Meta:
        model = CustomUser



# class CustomUserChangeForm(UserChangeForm):

#    class Meta:
#        model = CustomUser
#        fields = ('username', 'password')
#     #    fields = ('username', 'email')