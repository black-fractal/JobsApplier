from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}),
                               label='username',
                               required=True,
                               disabled=False,
                               help_text='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
                               label='password',
                               required=True,
                               disabled=False,
                               help_text='')

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginFormCaptcha(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}),
                               label='username',
                               required=True,
                               disabled=False,
                               help_text='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}),
                               label='password',
                               required=True,
                               disabled=False,
                               help_text='')

    captcha = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Security word'}),
                              label='Security word',
                              required=True,
                              disabled=False,
                              help_text='')

    class Meta:
        model = User
        fields = ['username', 'password', 'captcha']
