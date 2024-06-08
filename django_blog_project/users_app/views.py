from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm

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
            messages.success(request, f'Acount created for {username}')
            return redirect('blog-home')                    
    else:
        form = UserRegisterForm()
    
    return render(request, 'users_app/register.html', {'form': form})











"""Notes: form.save() does all this steps under the hood"""
#username = form.cleaned_data.get('username')
#password = form.cleaned_data.get('password1')
#new_user = User(username = username)
#new_user.set_password(password)
#new_user.save()