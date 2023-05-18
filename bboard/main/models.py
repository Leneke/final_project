from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Присылать сообщения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ['username', 'email', 'first_name', 'last_name', 'send_messages']

