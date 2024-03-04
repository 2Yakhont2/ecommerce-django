from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Obtener la llave de la sesion
        cart = self.session.get('session_key')

        # Si no existe, la creamos
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart

    # Funcion agregar
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)
        
        self.session.modified = True

    def cart_total(self):
        # Obtener el ids de los productos
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0

        for key, value in quantities.items():
            key = int(key)

            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
            
        return total


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Obtener los ids del carrito
        product_ids = self.cart.keys()
        # Usar los ids parar identificar los productos en la bd
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantity(self):
        quantities = self.cart
        return quantities
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True


