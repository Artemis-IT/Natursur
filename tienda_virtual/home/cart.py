"""
Utilidades para gestionar el carrito de compras usando sesiones de Django.
"""
from decimal import Decimal
from .models import Product


class Cart:
    
    def __init__(self, request):
        """Inicializa el carrito."""
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """Añade un producto al carrito o actualiza su cantidad."""
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'name': product.name,
                'image_url': product.image_url or '',
                'herbalife_url': product.herbalife_url,
            }
        
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()
    
    def save(self):
        """Marca la sesión como modificada para asegurar que se guarde."""
        self.session.modified = True
    
    def remove(self, product):
        """Elimina un producto del carrito."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def update_quantity(self, product_id, quantity):
        """Actualiza la cantidad de un producto específico."""
        product_id = str(product_id)
        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]['quantity'] = quantity
            else:
                del self.cart[product_id]
            self.save()
    
    def clear(self):
        """Elimina el carrito de la sesión."""
        del self.session['cart']
        self.save()
    
    def __iter__(self):
        """Itera sobre los items del carrito y obtiene los productos de la BD."""
        product_ids = self.cart.keys()
        # Obtenemos los productos de la base de datos
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_items(self):
        return len(self)
    
    def get_items(self):
        """Retorna una lista de items con información completa."""
        items = []
        for item in self:
            items.append({
                'product': item.get('product'),
                'quantity': item['quantity'],
                'name': item['name'],
                'image_url': item['image_url'],
                'herbalife_url': item['herbalife_url'],
            })
        return items