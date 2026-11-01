from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import redirect

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