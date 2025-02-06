from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from accounts.forms import *

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('cashier_dashboard')  # Redirect to home or another page after login
            else:
                form.add_error('email', 'Invalid email or password')
                messages.error(request, 'Invalid email or password. Please try again.')  # Error message
        return render(request, 'accounts/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main.html')

class ProfileView(View):
    def get(self, request):

        return render(request, 'accounts/profile.html')

    def post(self, request):

