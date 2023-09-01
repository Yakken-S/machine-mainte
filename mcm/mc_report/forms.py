from django import forms
from .models import Issue_History

class PostForm(forms.ModelForm):
    class Meta:
        model = Issue_History
        fields = '__all__'