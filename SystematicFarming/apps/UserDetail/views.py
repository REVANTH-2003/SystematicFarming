from django.shortcuts import render,redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import LoginForm

# Customized Login View - /auth/login

class Loginview(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'userdetail/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            return reverse('home')
        else:
            return reverse('login')
        

# Testing home page - /auth/home

@login_required
def home(request):
    return render(request, 'welcome.html')