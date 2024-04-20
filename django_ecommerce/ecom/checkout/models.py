from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save

class ShippingAddress(models.Model):
	# Asociar la direccion de envio con el usuario
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	
	shipping_full_name = models.CharField(max_length=100)
	shipping_address1 = models.CharField(max_length=30)
	shipping_address2 = models.CharField(max_length=30, blank=True)
	shipping_city = models.CharField(max_length=20)
	shipping_departments = models.CharField(max_length=30)


	# Asignar el nombre que tendra la clase 
	class Meta:
		verbose_name_plural = "Shipping Address"

	# Ver la direccion de envio desde el area del administrador	
	def __str__(self):
		return f'Shipping Address - {str(self.id)}'


# Crear una direccion de envio por defecto cuando un cliente se registra 
def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping, sender=User)


# Crear la tabla de la orden de los productos
class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	shipping_address = models.TextField(max_length=500)
	amount_paid = models.IntegerField()
	date_ordered = models.DateTimeField(auto_now_add=True)	

	def __str__(self):
		return f'Order - {str(self.id)}'



class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	quantity = models.PositiveBigIntegerField(default=1)
	price = models.IntegerField()


	def __str__(self):
		return f'Order Item - {str(self.id)}'