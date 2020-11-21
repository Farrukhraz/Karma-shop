from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms
from django.forms.widgets import HiddenInput, FileInput

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = str(field_name).title()


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = str(field_name).title()
            field.help_text = ''

    # любой валидатор должен начинаться с 'clean'. Т.е. clean_fieldName
    def clean_age(self):
        data = self.cleaned_data.get('age')
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = str(field_name).title()
            field.help_text = ''
            if field_name == "password":
                field.widget = HiddenInput()

    def clean_age(self):
        data = self.cleaned_data.get('age')
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data
