from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View


class View_signin(View):
	
	def get(self, request):
		return render(request, 'signin.html', {'form':UserCreationForm()})
	
	def post(self, request):
		f = UserCreationForm(request.POST)
		if f.is_valid():
			user = f.save()
			login(request, user)
			return redirect('main:home')
		else:
			for msg in f.error_messages:
				messages.error(request, f.error_messages[msg])
			return render(request, 'signin.html', {'form':f})

class View_login(View):
	def get(self, request): return render(request, 'login.html', {'form':AuthenticationForm()})
	def post(self, request):
		f = AuthenticationForm(request, request.POST)
		if f.is_valid():
			user = authenticate(username=f.cleaned_data.get('username'), password= f.cleaned_data.get('password'))
			if user is not None:
				login(request, user)
				return redirect('main:home')
			return redirect('/auth/login?wronguser')
		return redirect('/auth/login?invalid')

def logout_view(request): logout(request); return redirect('main:home')
