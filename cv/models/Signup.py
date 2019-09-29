from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               label='Username',
                               required=True,
                               disabled=False,
                               help_text='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
                                 label='First Name',
                                 required=True,
                                 disabled=False,
                                 help_text='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
                                label='Last Name',
                                required=True,
                                disabled=False,
                                help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                                label='Password',
                                required=True,
                                disabled=False,
                                help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}),
                                label='Repeat Password',
                                required=True,
                                disabled=False,
                                help_text='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}),
                             label='Email Address',
                             max_length=64,
                             help_text='<br>Please insert a valid email address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')