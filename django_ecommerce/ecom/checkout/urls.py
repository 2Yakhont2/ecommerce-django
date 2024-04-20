from django.urls import path
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('payment', views.payment, name='payment'),
    path('billing_information', views.billing_information, name="billing_information"),
]