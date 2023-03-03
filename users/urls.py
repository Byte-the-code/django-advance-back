from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_view, register

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/login.html'), name='logout'),
    path('register/', register, name='register'),
]