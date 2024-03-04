from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from .models import Product, Category, Profile
from .forms import SignUpForm, UserInfoForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


def about(request):
    return render(request, 'about-us.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Ocurrio un error, intentalo nuevamente"))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Regresa pronto"))
    return redirect('home')


def register_user (request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Cuenta registrada con exito. Por favor actualiza tus datos de contacto"))
            return redirect('update_info')
        else:
            messages.success(request, ("Ocurrió un error durante el registro de tu cuenta. Por favor intentalo nuevamente"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})


def product (request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


def update_info(request):
    # Solo disponible para usuarios que esten usando su cuenta
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Información actualizada")
            return redirect('home')
        return render(request, "update_info.html", {'form':form})
    else:
        messages.success(request, "Incia sesion")
        return redirect('home')
