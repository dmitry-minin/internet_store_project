from django.urls import path
from users.views import UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', next_page='catalog:home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),
]
