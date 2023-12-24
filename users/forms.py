from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import StyleFormMixin
from users.models import User
from users.signals import post_register


class UserProfileForm(StyleFormMixin, UserChangeForm):
	"""Добавление формы профиля пользователя"""
	class Meta:
		model = User
		fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar', 'country')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['password'].widget = forms.HiddenInput()


class RegisterForm(StyleFormMixin, UserCreationForm):
	"""Добавление формы регистрации пользователя с верификацией"""

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.is_active = False
		user.is_activated = False
		if commit:
			user.save()
		post_register.send(RegisterForm, instance=user)
		return user

	class Meta:
		model = User
		fields = ('first_name', 'email', 'password1', 'password2', 'avatar', 'phone', 'country',)
