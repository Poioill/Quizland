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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
