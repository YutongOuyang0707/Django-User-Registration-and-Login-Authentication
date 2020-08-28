from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


# Create your views here.
from .form import RegisterForm

# default one from visionX website
# def register(response):
# 	if response.method == "POST":
# 		form = UserCreationForm(response.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = UserCreationForm()
# 	return render(response, "register/register.html", {"form":form})

def register_page(request):
	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)


			return redirect('login')

	context = {'form':form}
	return render(request, 'register/register.html', context)


def login_page(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')


		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')


	context = {}
	return render(request, 'register/login.html', context)


def logout_page(request):
	logout(request)
	return redirect('login')
	# TODO: set the login/logout state in home page


