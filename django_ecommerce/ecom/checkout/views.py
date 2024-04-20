from django.shortcuts import render, redirect
from django.contrib import messages
from checkout.forms import ShippingForm
from checkout.models import ShippingAddress
from cart.cart import Cart


def payment_success(request):
    return render(request, "checkout/payment_success.html", {})

def payment(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quantity
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "checkout/payment.html", {"cart_products":cart_products,
                                                     "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        messages.success(request, "Incia sesion")
        return redirect('home')

def billing_information(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quantity
        totals = cart.cart_total()

        shipping = request.POST
        request.session['shipping'] = shipping

        if request.user.is_authenticated:
			#
            billing_form = PaymentForm()
            return render(request, "payment/billing_information.html", {"cart_products":cart_products,
                                                     "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
        
        else:
            billing_form = PaymentForm()
            return render(request, "payment/billing_information.html", {"cart_products":cart_products,
                                                     "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
    
    else:
	    return redirect('home')

