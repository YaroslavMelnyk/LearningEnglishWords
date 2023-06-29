from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy


#class UserForm(ModelForm):
#    class Meta:
#        model = User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Ім\'я користувача:', max_length=25)
    password = forms.CharField(label='Пароль:', max_length=50, widget=forms.PasswordInput)

    #class Meta:
    #    model = User
    #    fields = ['username', 'password']


class SingUpForm(UserCreationForm):
    username = forms.CharField(label='Ім\'я користувача')
    email = forms.EmailField(label='Електронна пошта')
    password1 = forms.CharField(
        label=gettext_lazy("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=gettext_lazy("Підтвердження паролю"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
         strip=False,
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        # "password1", "password2"