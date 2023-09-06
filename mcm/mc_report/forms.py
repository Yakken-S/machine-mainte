from django import forms
<<<<<<< HEAD
from .models import Issue_History
# from .models import Issue_History,CustomUser

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email')
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
=======
from .models import Issue_History,CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
>>>>>>> 63237a4161cd1471be41e140154dcb2f15bb5f6d

class PostForm(forms.ModelForm):
    class Meta:
        model = Issue_History
        fields = '__all__'
