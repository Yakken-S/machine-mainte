from django import forms
from .models import Issue_History


class PostForm(forms.ModelForm):
    class Meta:
        model = Issue_History
        fields = '__all__'


class SearchForm(forms.ModelForm):
    l1name = forms.CharField(
        initial='',
        label='l1_name',
        required = False, 
    )
    alarmnum = forms.CharField(
        initial='',
        label='alarm_num',
        required=False, 
    )