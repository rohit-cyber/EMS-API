from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse





def index(request):
	return render(request, 'index.html',{}) 

def signup(request):
	if request.method=="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		newuser = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username,
			password=password,
			email=email
			)
		try:
			newuser.save()
			return redirect('/signin')
		except:
			return HttpResponse("Something went wrong.")
	else:
		form = UserRegistrationForm()
		return render(request, 'signup.html',{'form':form})

def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is None:
			return HttpResponse("User not found.")
		login(request, user)
		return redirect('/')
	else:
		form = UserForm()
	return render(request, 'signin.html', {'form':form})

def signout(request):
	logout(request)
	return redirect('/')

