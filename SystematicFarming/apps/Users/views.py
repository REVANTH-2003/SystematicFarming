from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from .models import User

# Customized Login View - /auth/login

def Loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
                return redirect('login')
    else:
        form = LoginForm()
   
    return render(request, 'users/login.html', {'form': form })


# Register - /auth/register

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Log the user in after registration
            login(request, user)
            return redirect('home')
             # Redirect to the home page after successful registration

        else :
            messages.error(request, 'Enter a valid data !')
            return redirect('register')
           
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


# Testing home page - /auth/home
@login_required
def home(request):
    return render(request, 'welcome.html')