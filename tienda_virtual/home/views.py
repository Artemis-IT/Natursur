from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment, SecurityProfile, Product, Order, OrderItem
from .forms import AppointmentForm, RegistrationForm, LoginForm, CheckoutForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .cart import Cart
from django.db import transaction
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import json
from .send_sms import send_price_sms
from django.db.models import Sum, Count


def index(request):
	"""Vista para la pantalla de inicio (landing page) de Natursur."""
	
	# Obtener 3 productos aleatorios de Herbalife para destacados
	featured_products = Product.objects.filter(is_active=True).order_by('?')[:3]
	
	context = {
		'site_name': 'Natursur',
		'tagline': 'Nutrición natural para tu bienestar',
		'features': [
			{'title': 'Asesoría personal', 'desc': 'Planes nutricionales personalizados adaptados a tu estilo de vida.'},
			{'title': 'Productos naturales', 'desc': 'Suplementos y alimentos orgánicos seleccionados con calidad.'},
			{'title': 'Recetas saludables', 'desc': 'Ideas fáciles y nutritivas para tu día a día.'},
		],
		'featured_products': featured_products,
	}
	return render(request, 'home/index.html', context)


@login_required(login_url='home:login')
def appointments_list(request):
	"""Muestra las citas existentes y botón para crear nueva."""
	appointments = Appointment.objects.order_by('datetime')
	context = {
		'appointments': appointments,
		'site_name': 'Natursur'
	}
	return render(request, 'home/appointments.html', context)


@login_required(login_url='home:login')
def appointment_create(request):
	"""Formulario para crear una nueva cita."""
	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			ap = form.save()
			return redirect('home:citas_list')
	else:
		form = AppointmentForm()
	return render(request, 'home/appointment_form.html', {'form': form, 'site_name': 'Natursur'})


def register(request):
    """Registro simple que solicita nombre, apellidos, correo, contraseña y pregunta/resp. de seguridad."""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login automático tras registro
            user = authenticate(request, username=user.email, password=form.cleaned_data.get('password1'))
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Registro completado. Ya estás autenticado.')
                return redirect('home:products_list')
            else:
                messages.success(request, 'Registro completado. Inicia sesión.')
                return redirect('home:login')
    else:
        form = RegistrationForm()
    return render(request, 'home/register.html', {'form': form, 'site_name': 'Natursur'})


def login_view(request):
    """Login flexible: autenticar por email+password o email+security_question+answer."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            method = form.cleaned_data.get('login_method')
            
            # buscar usuario por email
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.filter(email__iexact=email).first()
            if not user:
                messages.error(request, 'Usuario no encontrado.')
                return render(request, 'home/login.html', {'form': form, 'site_name': 'Natursur'})
            
            if method == 'password':
                # autenticar con contraseña
                password = form.cleaned_data.get('password')
                user_auth = authenticate(request, username=user.email, password=password)
                if user_auth is not None:
                    auth_login(request, user_auth)
                    messages.success(request, f'Bienvenido {user.first_name}.')
                    return redirect('home:products_list')
                else:
                    messages.error(request, 'Contraseña incorrecta.')
            
            elif method == 'security':
                # autenticar con pregunta de seguridad
                answer = form.cleaned_data.get('security_answer')
                try:
                    sp = user.security_profile
                    if sp.check_answer(answer):
                        auth_login(request, user)
                        messages.success(request, f'Bienvenido {user.first_name}.')
                        return redirect('home:products_list')
                    else:
                        messages.error(request, 'Respuesta de seguridad incorrecta.')
                except SecurityProfile.DoesNotExist:
                    messages.error(request, 'No hay perfil de seguridad asociado.')
    else:
        form = LoginForm()
    
    return render(request, 'home/login.html', {'form': form, 'site_name': 'Natursur'})


def logout_view(request):
    """Logout del usuario."""
    auth_logout(request)
    messages.success(request, 'Has cerrado sesión.')
    return redirect('home:index')


def products_list(request):
    """Muestra el catálogo de productos de Herbalife con enlace a la web oficial."""
    
    # Obtener parámetro de búsqueda (opcional)
    search_query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    
    products = Product.objects.filter(is_active=True)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if category:
        products = products.filter(category__icontains=category)
    
    # Obtener categorías únicas para el filtro
    categories = Product.objects.filter(is_active=True).values_list('category', flat=True).distinct()
    
    # Obtener productos más pedidos por el usuario (si está autenticado)
    recommended_products = []
    if request.user.is_authenticated:
        recommended_products = get_user_recommended_products(request.user, limit=6)
    
    context = {
        'products': products,
        'search_query': search_query,
        'selected_category': category,
        'categories': [cat for cat in categories if cat],
        'site_name': 'Natursur',
        'total_products': products.count(),
        'recommended_products': recommended_products,
    }
    return render(request, 'home/products.html', context)


def cart_add(request, product_id):
    """Añade un producto al carrito."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    
    messages.success(request, f'"{product.name}" añadido al carrito.')
    
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'home:products_list'))
    return redirect(next_url)


def cart_detail(request):
    """Muestra el contenido del carrito."""
    cart = Cart(request)
    
    context = {
        'cart': cart,
        'site_name': 'Natursur',
    }
    return render(request, 'home/cart.html', context)


def cart_remove(request, product_id):
    """Elimina un producto del carrito."""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    
    messages.success(request, f'"{product.name}" eliminado del carrito.')
    return redirect('home:cart_detail')


def cart_update(request):
    """Actualiza las cantidades del carrito."""
    if request.method == 'POST':
        cart = Cart(request)
        
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                quantity = int(value)
                cart.update_quantity(product_id, quantity)
        
        messages.success(request, 'Carrito actualizado.')
    
    return redirect('home:cart_detail')


@login_required(login_url='home:login')
def checkout(request):
    """Vista para confirmar el pedido."""
    cart = Cart(request)
    
    if len(cart) == 0:
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('home:products_list')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Crear el pedido
                    order = Order.objects.create(
                        user=request.user,
                        customer_name=form.cleaned_data['customer_name'],
                        customer_email=form.cleaned_data['customer_email'],
                        customer_phone=form.cleaned_data['customer_phone'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        delivery_city=form.cleaned_data['delivery_city'],
                        delivery_postal_code=form.cleaned_data['delivery_postal_code'],
                        notes=form.cleaned_data['notes'],
                    )
                    
                    # Crear los items del pedido
                    for item in cart:
                        OrderItem.objects.create(
                            order=order,
                            product=item['product'],
                            quantity=item['quantity'],
                            product_name=item['name'],
                            product_url=item['herbalife_url'],
                        )
                    
                    cart.clear()
                    
                    messages.success(
                        request, 
                        f'¡Pedido #{order.id} confirmado! Recibirás un correo de confirmación pronto.'
                    )
                    return redirect('home:order_detail', order_id=order.id)
            
            except Exception as e:
                messages.error(request, f'Error al procesar el pedido: {str(e)}')
    else:
        initial_data = {
            'customer_name': f"{request.user.first_name} {request.user.last_name}".strip(),
            'customer_email': request.user.email,
        }
        form = CheckoutForm(initial=initial_data)
    
    context = {
        'form': form,
        'cart': cart,
        'site_name': 'Natursur',
    }
    return render(request, 'home/checkout.html', context)


@login_required(login_url='home:login')
def order_detail(request, order_id):
    """Muestra los detalles de un pedido específico."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
        'site_name': 'Natursur',
    }
    return render(request, 'home/order_detail.html', context)


@login_required(login_url='home:login')
def orders_list(request):
    """Lista todos los pedidos del usuario."""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
        'site_name': 'Natursur',
    }
    return render(request, 'home/orders_list.html', context)


def get_user_recommended_products(user, limit=6):
    """
    Obtiene los productos más pedidos por el usuario.
    Retorna una lista de diccionarios con producto y cantidad total pedida.
    """
    most_ordered = OrderItem.objects.filter(
        order__user=user
    ).values(
        'product__id',
        'product__name',
        'product__image_url',
        'product__herbalife_url'
    ).annotate(
        total_quantity=Sum('quantity'),
        times_ordered=Count('id')
    ).order_by('-total_quantity')[:limit]
    
    recommended = []
    for item in most_ordered:
        try:
            product = Product.objects.get(id=item['product__id'])
            recommended.append({
                'product': product,
                'total_quantity': item['total_quantity'],
                'times_ordered': item['times_ordered']
            })
        except Product.DoesNotExist:
            continue
    
    return recommended


@login_required(login_url='home:login')
def repeat_order(request, order_id):
    """Añade todos los productos de un pedido anterior al carrito."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    cart = Cart(request)
    
    # Añadir cada item del pedido al carrito
    items_added = 0
    for item in order.items.all():
        try:
            # Verificar que el producto siga activo
            if item.product.is_active:
                cart.add(product=item.product, quantity=item.quantity)
                items_added += 1
        except Exception as e:
            messages.warning(request, f'No se pudo añadir "{item.product_name}": {str(e)}')
    
    if items_added > 0:
        messages.success(
            request, 
            f'¡Pedido repetido! Se añadieron {items_added} productos al carrito.'
        )
    else:
        messages.warning(request, 'No se pudo añadir ningún producto del pedido.')
    
    return redirect('home:cart_detail')

@staff_member_required
def manage_orders(request):
    """Vista para que el superusuario gestione pedidos y envíe precios por SMS."""
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('home:index')
    
    # Obtener pedidos pendientes o en proceso
    orders = Order.objects.filter(
        status__in=['pending', 'processing']
    ).order_by('-created_at')
    
    context = {
        'orders': orders,
        'site_name': 'Natursur',
    }
    return render(request, 'home/manage_orders.html', context)


@staff_member_required
def update_order_price(request, order_id):
    """Envía SMS con el precio al cliente (sin guardar en BD)."""
    if not request.user.is_superuser:
        return JsonResponse({'success': False, 'error': 'Sin permisos'}, status=403)
    
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)
    
    try:
        order = get_object_or_404(Order, id=order_id)
        data = json.loads(request.body)
        price = data.get('price')
        
        if not price:
            return JsonResponse({'success': False, 'error': 'Precio requerido'}, status=400)
        
        # Enviar SMS usando función del módulo send_sms
        success = send_price_sms(order, float(price))
        
        if success:
            # Guardar en sesión que ya se envió (opcional)
            if 'notified_orders' not in request.session:
                request.session['notified_orders'] = []
            request.session['notified_orders'].append(order_id)
            request.session.modified = True
            
            return JsonResponse({
                'success': True, 
                'message': f'SMS enviado a {order.customer_phone} con precio {price}€'
            })
        else:
            return JsonResponse({
                'success': False, 
                'error': 'Falló el envío de SMS'
            }, status=500)
            
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)