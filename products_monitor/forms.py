from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # discord = forms.CharField(label="Discord")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'discord']

class CustomUserChangeForm(UserChangeForm):
    # discord = forms.CharField(label="Discord")

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'discord']
