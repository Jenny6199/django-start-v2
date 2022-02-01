import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import forms, ModelForm

from .models import ShopUser
from .models import ShopUserProfile


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("18+ Доступ запрещен! Возвращайтесь когда Вам исполнится 18 лет.")
        return data

    def save(self):
        user = super(ShopUserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                pass

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("18+ Доступ запрещен! Возвращайтесь когда Вам исполнится 18 лет.")
        return data


class ShopUserProfileEditForm(ModelForm):
    """Редактирование профиля пользователя"""
    class Meta:
        model = ShopUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

        def __init__(self, *args, **kwargs):
            super(ShopUserProfileEditForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
