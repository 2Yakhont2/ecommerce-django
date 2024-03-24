from django.shortcuts import render


def payment_success(request):
    return render(request, "checkout/payment_success.html", {})
