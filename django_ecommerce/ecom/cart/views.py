from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart


# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quantity
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals})

def cart_add(request):
    cart = Cart(request)

    # Probar el POST
    if request.POST.get('action') == 'post':

        # Obtener los productos
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        # Buscar productos en la base de datos
        product = get_object_or_404(Product, id=product_id)

        # Guardar la sesion
        cart.add(product=product, quantity=product_quantity)

        # Obtener el numero de productos dentro del carrito
        cart_quantity = cart.__len__()

        # Retornar la respuesta
        response = JsonResponse({'quantity': cart_quantity})
        return response


def cart_update(request):
    pass

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response
