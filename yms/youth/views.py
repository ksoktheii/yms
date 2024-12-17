from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import ProfileUpdateForm, UserUpdateForm 
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

@login_required
def profile_update(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Update user details
            profile_form.save()  # Update profile details
            return redirect('profile-display')  # Redirect to the profile page to display updated info
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile_update.html', {'user_form': user_form, 'profile_form': profile_form})

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
