"""
Context processors para la aplicación home.
Permite que ciertas variables estén disponibles en todas las plantillas.
"""
from .cart import Cart


def cart_context(request):
    """
    Añade el carrito a todas las plantillas.
    Esto permite usar {{ cart|length }} en cualquier template.
    """
    return {
        'cart': Cart(request)
    }
