import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Usamos el modelo User de Django para crear los usuarios. El modelo 
# User tiene 5 atributos por defecto: username, password, email, first_name, last_name

# Para agregar mas atributos a User hay que crear un Profile y asociarlo con User 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Informacion adicional de la cuenta de usuario
    city = models.CharField(max_length=20)
    departments = models.CharField(max_length=30)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username

  
# Crear un perfil de usuario por defecto cuando se crea una nueva cuenta 
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    # Se nombra manualmente la clase como Categories
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return  f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', default='uploads/product/default.png')

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
