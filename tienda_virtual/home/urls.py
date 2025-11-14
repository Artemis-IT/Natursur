from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.products_list, name='products_list'),
    path('citas/', views.appointments_list, name='citas_list'),
    path('citas/nueva/', views.appointment_create, name='citas_create'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('carrito/', views.cart_detail, name='cart_detail'),
    path('carrito/añadir/<int:product_id>/', views.cart_add, name='cart_add'),
    path('carrito/eliminar/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('carrito/actualizar/', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('pedidos/', views.orders_list, name='orders_list'),
    path('pedidos/<int:order_id>/', views.order_detail, name='order_detail'),
]
