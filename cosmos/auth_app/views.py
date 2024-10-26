from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from uni_app.models import Cat


class View_signin(View):
	
	def get(self, request):
		return render(request, 'signin.html', {'form':UserCreationForm(), 'cats':Cat.objects.all()})
	
	def post(self, request):
		f = UserCreationForm(request.POST)
		if f.is_valid():
			user = f.save()
			login(request, user)
			return redirect('main:home')
		else:
			for msg in f.error_messages:
				messages.error(request, f.error_messages[msg])
			return render(request, 'signin.html', {'form':f, 'cats':Cat.objects.all()})

class View_login(View):
	def get(self, request): return render(request, 'login.html', {'form':AuthenticationForm(), 'cats':Cat.objects.all()})
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

@login_required(login_url='auth:login')
def profile_view(request):
	return render(request, 'profile.html', {'cats':Cat.objects.all()})
