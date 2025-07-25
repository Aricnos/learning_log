from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """ Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """  Register a new user. """
    try:
        if request.method != 'POST':
            # Display blank registration form
            form = UserCreationForm()
        else:
            # Process completer form
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                # log in and the reddirect to home page
                authenticated_user = authenticate(username=new_user.username, password= request.POST['password1'])
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('learning_logs:index'))
            
        context ={'form':form} 
        return render(request, 'users/register.html', context)
    except Exception as e:
        print(f"ERROR: {e}")
        raise  # re-raise for logging
            
    