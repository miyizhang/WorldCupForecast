from django import forms
from .models import MatchInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MatchInfoForm(forms.ModelForm):
    match_date = forms.CharField(label='比赛日期', max_length=50)
    match_time = forms.CharField(label='比赛时间', max_length=50)
    team_a = forms.CharField(label='主队', max_length=50)
    team_b = forms.CharField(label='客队', max_length=50)
    result = forms.CharField(label='结果', max_length=50)

    class Meta:
        model = MatchInfo
        fields = ['match_date', 'match_time', 'team_a', 'team_b', 'result']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
