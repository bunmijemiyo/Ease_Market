from django.shortcuts import render

# Create your views here.
from django.views import View



class ProfileView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'seller/index.html')
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views import View
from django.views.generic import CreateView

# Create your views here.

class MenuView(View):
	
	def get(self, request, *args, **kwargs):

		return render(request, 'menu/menu_page.html')

class ProfileView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'home.html')

class CustomLoginView(LoginView):
	template_name = 'login.html'
	fields = '__all__'
	redirect_authenticated_user = False

	def get_success_url(self):
		return reverse_lazy('menu')

class RegisterPage(FormView):
	template_name = 'register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('menu')
		return super(RegisterPage, self).get(*args, **kwargs)


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'


class LoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = '/'
    template_name = 'login.html'


def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# log the user in
			user = form.save()
			login(request, user)
			return redirect('login')
	form = UserCreationForm()
	context = {'form': form}
	return render(request, 'register.html', context)

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			# log the user in
			login(request, user)
			return redirect('menu')
		
	form = AuthenticationForm()
	context = {'form': form}
	return render(request, 'login.html', context)


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('menu')
"""
