from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Event

def home(request):
	events = Event.objects
	return render(request, 'events/home.html', {'events': events})

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'events/signupuser.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('home')
			except IntegrityError:
				return render(request, 'events/signupuser.html', {'form':UserCreationForm(), 'error': 'That username has already been taken. Please choose another one.'})
		else:
			return render(request, 'events/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'events/loginuser.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'events/loginuser.html', {'form':AuthenticationForm(), 'error': 'Username and password did not match'})
		else:
			login(request, user)
			return redirect('home')

def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')
