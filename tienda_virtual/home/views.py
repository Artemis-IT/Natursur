from django.shortcuts import render


def index(request):
	"""Vista para la pantalla de inicio (landing page) de Natursur."""
	from .models import Product
	
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


from django.shortcuts import redirect, get_object_or_404
from .models import Appointment, SecurityProfile
from .forms import AppointmentForm, RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout




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
                return redirect('home:citas_list')
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
                    return redirect('home:citas_list')
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
                        return redirect('home:citas_list')
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
    from .models import Product
    
    # Obtener parámetro de búsqueda (opcional)
    search_query = request.GET.get('q', '').strip()
    
    products = Product.objects.filter(is_active=True)
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    context = {
        'products': products,
        'search_query': search_query,
        'site_name': 'Natursur',
        'total_products': products.count()
    }
    return render(request, 'home/products.html', context)

