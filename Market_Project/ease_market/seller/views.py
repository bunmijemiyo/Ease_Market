from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CreateSeller
from .models import Seller
from django.contrib import messages


# Create your views here.
from django.views import View



class ProfileView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'home.html')


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
			return redirect('home')
		return super(RegisterPage, self).get(*args, **kwargs)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'seller/register.html'

class LoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = False
    success_url = '/seller'
    template_name = 'seller/login.html'


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')


@login_required(login_url='/login') # This ensures user is login before he can access this page
def seller_create(request):
	form = CreateSeller()
	if request.method == 'POST':
		form = CreateSeller(request.POST, request.FILES)
		# if request.user.is_staff:
		# 	return HttpResponseForbidden(status=403)
		if form.is_valid():
			instance = form.save(commit=False) # This allows us to get & do something with the item b4 saving it
			instance.author = request.user # Helps to attach the currently login user as author of the article
			instance.save()
			#print(my_form.cleaned_data)
			# print(**my_form.cleaned_data)
			#Products_2.objects.create(**my_form.cleaned_data)
			messages.info(request, "Product Created Successfully.")
			return redirect('seller:home')
		messages.error(request, "Something went wrong with creating products.")
	context = {'form': form}
	return render(request, 'seller/create_product.html', context)


class SellerListView(View):
	def get(self, request, *args, **kwargs):
		sellers = Seller.objects.all()
		context = {'sellers': sellers }
		return render(request, 'seller/seller_list.html', context)

def seller_detail(request, slug):
	#return HttpResponse(slug)
	seller = Seller.objects.get(slug=slug)
	context = {'seller': seller}
	return render(request, 'seller/seller_detail.html', context)

"""


from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm

from django.views import View


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



"""
