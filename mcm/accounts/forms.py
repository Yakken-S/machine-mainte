from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import CustomUser

class CustomUserCreationForm(SignupForm):
    username = forms.CharField(max_length=5, required=True, label="従業員番号")
    user_name = forms.CharField(max_length=50, required=True, label="氏名")
    
    def save(self, request):
        user = super().save(request)
        user.username = self.cleaned_data['username']
        user.user_name = self.cleaned_data['user_name']
        user.save()
        return user
    
    class Meta:
        model = CustomUser
        fields = ('username', 'user_name')

class CustomUserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        login_widget = forms.TextInput(
                attrs={"placeholder": "従業員番号", "autocomplete": "username"}
            )
        self.fields["login"] = forms.CharField(label="従業員番号", max_length=5, widget=login_widget)
