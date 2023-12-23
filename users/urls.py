from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, RegisterDoneView, user_activate

app_name = UsersConfig.name

urlpatterns = [
		path('', LoginView.as_view(), name='login'),
		path('logout/', LogoutView.as_view(), name='logout'),
		path('accounts/register/', RegisterView.as_view(), name='register'),
		path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
		path('accounts/activate/<str:sign>', user_activate, name='activate'),
]
