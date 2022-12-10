from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'data', 'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'data', 'placeholder': 'Password'}
        )
        self.fields['username'].label = ""
        self.fields['password'].label = ""


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
        labels = {
            'username': '',
            'email': '',
            'age': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'data', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'data', 'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'class': 'data', 'placeholder': 'Age'}),
        }
        help_texts = {
            'username': None,
        }
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'data', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'data', 'placeholder': 'Confirm password'}))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
