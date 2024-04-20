from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from checkout.forms import ShippingForm
from checkout.models import ShippingAddress

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages

from .models import Product, Category, Profile
from .forms import SignUpForm, UserInfoForm


# Hace una consulta a la tabla Product en SQL y almacena la informacion en products
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


# Renderizar la plantilla about-us.html
def about(request):
    return render(request, 'about-us.html', {})


def login_user(request):
    # Al presionar el boton Ingresa el formulario de login envia una peticion post al servidor
    if request.method == "POST":
        # Se busca obtener el valor de los inputs name=username y name=password"
        username = request.POST['username']
        password = request.POST['password']
        # Usamos el sistema de autenticacion de django para comprobar si existe el usuario 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error: Usuario o Contraseña incorrecto!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


# Para usar el metodo redirect necesitamos importarlo de django.shortcuts
def logout_user(request):
    logout(request)
    messages.success(request, ("Regresa pronto"))
    # Como argumento del metodo redirect se pasa la url a la que sera redirigido
    return redirect('home')


# Maneja el formulario form y el envio de datos al servidor
def register_user (request):
    form = SignUpForm()
    if request.method == "POST":
        # Guardamos en form la informacion que se envio en el formulario SignUpForm 
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


# Hacemos una consulta a la tabla product para obtener la llave primaria de cada producto
def product (request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})


# Solo disponible para usuarios que esten usando su cuenta
def update_info(request):
    if request.user.is_authenticated:
        # Obtener el usuario actual
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        
        # Obtener la orden del usuario
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        
        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Información actualizada")
            return redirect('home')
        return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
    else:
        messages.success(request, "Incia sesion")
        return redirect('home')
