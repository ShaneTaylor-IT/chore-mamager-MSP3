from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(
        request,
        'core/landing.html',        
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = RegistrationForm()

    return render(
        request,
        'core/registration.html',
        {'form': form}
    )

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing_page')
    else:
        form = AuthenticationForm()

    return render(
        request,
        'core/login.html',
        {'form': form}
    )

def user_logout(request):
    logout(request)
    return redirect('landing_page')

@login_required
def dashboard(request):
    return render(
        request,
        'core/dashboard.html',
    )

