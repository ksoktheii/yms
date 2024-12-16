from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Set session variable to show profile update popup
            request.session['show_profile_popup'] = True
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_user')

@login_required
def user_dashboard(request):
    # Check if the user needs to see the profile update popup
    show_popup = request.session.get('show_profile_popup', False)
    # Optionally reset the session flag once they view the dashboard
    if show_popup:
        request.session['show_profile_popup'] = False

    return render(request, 'dashboard.html', {'show_popup': show_popup})

@login_required
def profile(request):
    user_profile = request.user.profile  # Get the user's profile
    return render(request, 'profile.html', {'user_profile': user_profile})

def profile_update(request):
    user_profile = request.user.profile  # Assuming the user has a profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # Save profile updates
            form.save()
            # Handle password change if provided
            password = form.cleaned_data.get('password')
            if password:
                user = request.user
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)  # Keep user logged in after password change

            return redirect('profile-display')  # Redirect after successful update
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'profile_update.html', {'form': form})

def sign_in(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Set session variable to show profile update popup after login
                request.session['show_profile_popup'] = True
                return redirect('user_dashboard')
            else:
                msg.append('Your account has been deactivated!')
    else:
        msg.append('Invalid login credentials, try again!')
    return render(request, 'login.html', {'errors': msg})
