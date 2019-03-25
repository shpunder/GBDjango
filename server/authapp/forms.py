from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import ShopUser




class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
        widgets = {
            'username': forms.widgets.TextInput(
                attrs={'class': 'form-control'}
            ),
            'password': forms.widgets.TextInput(
                attrs={'class': 'form-control'}
            )
        }


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
            'password': None,
            }


    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    def clean_email(self):
        data = self.cleaned_data['first_name']
        if data == 'Имя':
            raise forms.ValidationError("Это не Ваше имя!")

        return data
