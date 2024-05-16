from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

'''@login_required
def user_profile(request):
    # Your profile view logic here
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})'''

def profile(request):
    return render(request, 'profile.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the homepage or any other desired page
                return redirect('home')
            else:
                # Invalid username or password
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})
