from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def landing_page(request):
    return render(
        request,
        'core/landing.html',        
    )

def register(request):
    form = RegistrationForm()

    return render(
        request,
        'core/registration.html',
        {'form': form}
    )