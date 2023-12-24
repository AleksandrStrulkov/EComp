from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView

from catalog.forms import StyleFormMixin
from users.models import User
from django.urls import reverse_lazy

from users.forms import RegisterForm, UserProfileForm

from django.core.signing import BadSignature
from .utilities import signer
from django.views.decorators.csrf import csrf_exempt


class LoginView(BaseLoginView):
	template_name = 'users/login.html'



class LogoutView(BaseLogoutView):
	pass


class RegisterView(CreateView):
	model = User
	# form_class = UserForm
	form_class = RegisterForm
	success_url = reverse_lazy('users:register_done')
	template_name = 'users/register.html'
	success_message = 'Вы успешно зарегистрировались'


class RegisterDoneView(TemplateView):
	template_name = 'users/register_done.html'


# @csrf_exempt
def user_activate(request, sign):
	try:
		email = signer.unsign(sign)
	except BadSignature:
		return render(request, 'users/activation_failed.html')

	user = get_object_or_404(User, email=email)

	if user.is_activated:
		template = 'users/activation_done_earlier.html'
	else:
		template = 'users/activation_done.html'
		user.is_active = True
		user.is_activated = True
		user.save()

	return render(request, template)


class UserUpdateView(UpdateView):
	models = User
	success_url = reverse_lazy('users:profile')
	form_class = UserProfileForm

	def get_object(self, queryset=None): # Избавляемся от входящего параметра pk
		return self.request.user


