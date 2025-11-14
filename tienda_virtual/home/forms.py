from django import forms
from .models import Appointment

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import SecurityProfile
from django.db import transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils import timezone


User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nombre', max_length=150, required=True)
    last_name = forms.CharField(label='Apellidos', max_length=150, required=True)
    # Predefined security questions - user selects one
    SECURITY_QUESTIONS = [
        ('¿Cuál es el nombre de tu primera mascota?', '¿Cuál es el nombre de tu primera mascota?'),
        ('¿Cuál es el nombre de tu escuela primaria?', '¿Cuál es el nombre de tu escuela primaria?'),
        ('¿Cuál es el nombre de tu mejor amigo de la infancia?', '¿Cuál es el nombre de tu mejor amigo de la infancia?'),
        ('¿En qué ciudad naciste?', '¿En qué ciudad naciste?'),
        ('¿Cuál es el segundo nombre de tu padre?', '¿Cuál es el segundo nombre de tu padre?'),
        ('¿Cuál era tu apodo de niño?', '¿Cuál era tu apodo de niño?'),
        ('¿Cuál fue tu primer coche?', '¿Cuál fue tu primer coche?'),
        ('¿Cuál es tu comida favorita?', '¿Cuál es tu comida favorita?'),
        ('¿Cuál es el nombre de tu primer jefe?', '¿Cuál es el nombre de tu primer jefe?'),
        ('¿Cuál fue el nombre de tu primer profesor?', '¿Cuál fue el nombre de tu primer profesor?'),
        ('¿En qué ciudad se conocieron tus padres?', '¿En qué ciudad se conocieron tus padres?'),
        ('¿Cuál fue tu juguete favorito de la infancia?', '¿Cuál fue tu juguete favorito de la infancia?'),
    ]
    security_question = forms.ChoiceField(label='Pregunta de seguridad', choices=SECURITY_QUESTIONS, required=True)
    security_answer = forms.CharField(label='Respuesta', max_length=255, required=True)

    class Meta:
        model = User
        # We don't ask for a separate username; we'll use the email as username
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza los mensajes de error de las contraseñas al español
        self.fields['password1'].help_text = (
            '<ul>'
            '<li>Tu contraseña no puede ser muy parecida a tu información personal.</li>'
            '<li>Tu contraseña debe tener al menos 8 caracteres.</li>'
            '<li>Tu contraseña no puede ser un número completamente.</li>'
            '<li>Evita contraseñas muy comunes.</li>'
            '</ul>'
        )
        self.fields['password1'].error_messages = {
            'required': 'La contraseña es obligatoria.',
            'invalid': 'Ingresa una contraseña válida.',
        }
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['password2'].error_messages = {
            'required': 'Confirma tu contraseña.',
            'invalid': 'Ingresa una contraseña válida.',
        }

    def clean_email(self):
        """Ensure email is unique among users."""
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Ya existe una cuenta con este correo.')
        return email

    def clean_password2(self):
        """Check that both passwords match and meet requirements."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError('Las contraseñas no coinciden.')
        return password2

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # use email as username to avoid asking separate username
        user.username = self.cleaned_data.get('email')
        if commit:
            user.save()
            # crear perfil de seguridad (respuesta guardada hasheada)
            raw_answer = self.cleaned_data.get('security_answer')
            hashed = make_password(raw_answer)
            SecurityProfile.objects.create(
                user=user,
                question=self.cleaned_data.get('security_question'),
                answer=hashed
            )
        return user


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'datetime', 'notes']
        widgets = {
            # Use a text input that will be enhanced by a JS datetime picker (flatpickr)
            'datetime': forms.TextInput(attrs={'class': 'input datetimepicker', 'autocomplete': 'off', 'placeholder': 'YYYY-MM-DD HH:MM'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
        }

    def clean_datetime(self):
        """Ensure the selected datetime is in the future (server-side validation)."""
        dt = self.cleaned_data.get('datetime')
        if dt:
            # Compare with current time (timezone-aware)
            now = timezone.now()
            if dt < now:
                raise ValidationError('La fecha y hora deben ser en el futuro.')
        return dt


class LoginForm(forms.Form):
    """Flexible login form: choose between email+password or security question."""
    LOGIN_METHODS = (
        ('password', 'Correo y contraseña'),
        ('security', 'Pregunta de seguridad'),
    )
    
    email = forms.EmailField(label='Correo', required=True)
    login_method = forms.ChoiceField(
        label='Elige cómo iniciar sesión',
        choices=LOGIN_METHODS,
        widget=forms.RadioSelect,
        required=True
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        required=False,
        max_length=128
    )
    security_answer = forms.CharField(
        label='Respuesta de seguridad',
        required=False,
        max_length=255
    )

    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get('login_method')
        password = cleaned_data.get('password')
        security_answer = cleaned_data.get('security_answer')

        if method == 'password' and not password:
            self.add_error('password', 'La contraseña es obligatoria si eliges este método.')
        elif method == 'security' and not security_answer:
            self.add_error('security_answer', 'La respuesta es obligatoria si eliges este método.')

        return cleaned_data
    
    
class CheckoutForm(forms.Form):
    """Formulario para completar un pedido."""
    
    customer_name = forms.CharField(
        label='Nombre completo',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Juan Pérez'})
    )
    
    customer_email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'juan@ejemplo.com'})
    )
    
    customer_phone = forms.CharField(
        label='Teléfono de contacto',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': '+34 600 000 000'})
    )
    
    delivery_address = forms.CharField(
        label='Dirección de entrega',
        widget=forms.Textarea(attrs={'class': 'textarea', 'rows': 3, 'placeholder': 'Calle, número, piso, puerta...'})
    )
    
    delivery_city = forms.CharField(
        label='Ciudad',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Alcalá de Guadaíra'})
    )
    
    delivery_postal_code = forms.CharField(
        label='Código postal',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': '41500'})
    )
    
    notes = forms.CharField(
        label='Información adicional',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'textarea', 
            'rows': 4, 
            'placeholder': 'Instrucciones de entrega, preferencias, etc.'
        })
    )
    
    def clean_customer_phone(self):
        """Valida el formato del teléfono si se proporciona."""
        phone = self.cleaned_data.get('customer_phone')
        if phone:
            # Eliminar espacios y guiones
            phone_cleaned = phone.replace(' ', '').replace('-', '')
            # Validación básica: debe contener principalmente dígitos
            if not phone_cleaned.replace('+', '').isdigit():
                raise ValidationError('Introduce un número de teléfono válido.')
        return phone
