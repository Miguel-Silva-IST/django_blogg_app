from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    """Shows form for user creation for get request on endpoint
        If form is filled and submit button is pressed then a 
        post request is sent to the same url. If post request 
        is detected the backend saves the new_user to the User model
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()       
            messages.success(request, f'Your acount has been created')
            return redirect('login')                    
    else:
        form = UserRegisterForm()
    
    return render(request, 'users_app/register.html', {'form': form})


@login_required
def profile(request):
    
    if request.method == 'POST':    
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form':u_form,
        'p_form': p_form
    }
    
    return render(request, 'users_app/profile.html', context)











"""Notes: form.save() does all this steps under the hood"""
#username = form.cleaned_data.get('username')
#password = form.cleaned_data.get('password1')
#new_user = User(username = username)
#new_user.set_password(password)
#new_user.save()