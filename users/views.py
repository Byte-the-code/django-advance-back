from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.dispatch import receiver

from users.forms import RegisterForm
from users.models import UserProfile

def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            context = {
                'errors': form.errors,
            }
            return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'errors': form.errors,
            }
            return render(request, 'users/register.html', context)

def users_list_view(request):
    return render(request, 'users/users_list.html')

def user_profile_view(request):
    return render(request, 'users/user_profile.html')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
