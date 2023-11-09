from django import forms
from .models import Issue_History,Alarm

class PostForm(forms.ModelForm):
    class Meta:
        model = Issue_History
        fields = '__all__'

class SearchForm(forms.Form):
    alarm_num = forms.ModelChoiceField(
        queryset=Alarm.objects.all(),
        initial='',
        label='alarm_num',
        required=False, 
    )
    text = forms.CharField(
        initial='',
        label='text',
        required=False, 
    )