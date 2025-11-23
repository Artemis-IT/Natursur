from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from unittest.mock import patch, MagicMock

from .models import Appointment, SecurityProfile, Product, Order, OrderItem
from .forms import AppointmentForm, RegistrationForm, LoginForm, CheckoutForm
from .cart import Cart


User = get_user_model()


# ============================================================
# TESTS DE MODELOS
# ============================================================

class AppointmentModelTest(TestCase):
    """Pruebas unitarias para el modelo Appointment."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.appointment = Appointment.objects.create(
            name="Juan Pérez",
            email="juan@example.com",
            datetime=timezone.now() + timedelta(days=1),
            notes="Primera cita"
        )
    
    def test_appointment_creation(self):
        """Verifica que se crea correctamente una cita."""
        self.assertIsNotNone(self.appointment.id)
        self.assertEqual(self.appointment.name, "Juan Pérez")
        self.assertEqual(self.appointment.email, "juan@example.com")
        self.assertEqual(self.appointment.notes, "Primera cita")
    
    def test_appointment_str_representation(self):
        """Verifica la representación string del modelo."""
        expected = f"{self.appointment.name} — {self.appointment.datetime:%Y-%m-%d %H:%M}"
        self.assertEqual(str(self.appointment), expected)
    
    def test_appointment_ordering(self):
        """Verifica que las citas se ordenan por datetime descendente."""
        appointment2 = Appointment.objects.create(
            name="María López",
            email="maria@example.com",
            datetime=timezone.now() + timedelta(days=2)
        )
        appointments = Appointment.objects.all()
        self.assertEqual(appointments[0], appointment2)
        self.assertEqual(appointments[1], self.appointment)
    
    def test_appointment_blank_notes(self):
        """Verifica que las notas pueden estar vacías."""
        appointment = Appointment.objects.create(
            name="Pedro García",
            email="pedro@example.com",
            datetime=timezone.now()
        )
        self.assertEqual(appointment.notes, "")


class SecurityProfileModelTest(TestCase):
    """Pruebas unitarias para el modelo SecurityProfile."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.user = User.objects.create_user(
            username="testuser@example.com",
            email="testuser@example.com",
            password="TestPassword123",
            first_name="Test",
            last_name="User"
        )
        from django.contrib.auth.hashers import make_password
        self.security_profile = SecurityProfile.objects.create(
            user=self.user,
            question="¿Cuál es tu color favorito?",
            answer=make_password("azul")
        )
    
    def test_security_profile_creation(self):
        """Verifica que se crea correctamente un perfil de seguridad."""
        self.assertIsNotNone(self.security_profile.id)
        self.assertEqual(self.security_profile.user, self.user)
        self.assertEqual(self.security_profile.question, "¿Cuál es tu color favorito?")
    
    def test_security_profile_str_representation(self):
        """Verifica la representación string del modelo."""
        expected = f"Security for {self.user.get_username()}"
        self.assertEqual(str(self.security_profile), expected)
    
    def test_check_answer_correct(self):
        """Verifica que check_answer valida correctamente una respuesta correcta."""
        self.assertTrue(self.security_profile.check_answer("azul"))
    
    def test_check_answer_incorrect(self):
        """Verifica que check_answer rechaza una respuesta incorrecta."""
        self.assertFalse(self.security_profile.check_answer("rojo"))
    
    def test_one_to_one_relationship(self):
        """Verifica que un usuario solo puede tener un perfil de seguridad."""
        self.assertEqual(self.user.security_profile, self.security_profile)


class ProductModelTest(TestCase):
    """Pruebas unitarias para el modelo Product."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.product = Product.objects.create(
            name="Aloe Vera Gel",
            herbalife_url="https://example.com/product1",
            image_url="https://example.com/image1.jpg",
            description="Gel de aloe vera natural",
            category="Suplementos",
            is_active=True
        )
    
    def test_product_creation(self):
        """Verifica que se crea correctamente un producto."""
        self.assertIsNotNone(self.product.id)
        self.assertEqual(self.product.name, "Aloe Vera Gel")
        self.assertEqual(self.product.category, "Suplementos")
        self.assertTrue(self.product.is_active)
    
    def test_product_str_representation(self):
        """Verifica la representación string del modelo."""
        self.assertEqual(str(self.product), "Aloe Vera Gel")
    
    def test_product_ordering(self):
        """Verifica que los productos se ordenan por nombre."""
        product2 = Product.objects.create(
            name="Batido Nutricional",
            herbalife_url="https://example.com/product2"
        )
        products = Product.objects.all()
        self.assertEqual(products[0], self.product)
        self.assertEqual(products[1], product2)
    
    def test_product_unique_url(self):
        """Verifica que la URL de Herbalife debe ser única."""
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                name="Producto Duplicado",
                herbalife_url="https://example.com/product1"
            )
    
    def test_product_optional_fields(self):
        """Verifica que los campos opcionales pueden estar vacíos."""
        product = Product.objects.create(
            name="Producto Simple",
            herbalife_url="https://example.com/simple"
        )
        self.assertEqual(product.image_url, None)
        self.assertEqual(product.description, "")
        self.assertEqual(product.category, "")


class OrderModelTest(TestCase):
    """Pruebas unitarias para el modelo Order."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.user = User.objects.create_user(
            username="orderuser@example.com",
            email="orderuser@example.com",
            password="TestPass123"
        )
        self.product1 = Product.objects.create(
            name="Producto 1",
            herbalife_url="https://example.com/p1"
        )
        self.product2 = Product.objects.create(
            name="Producto 2",
            herbalife_url="https://example.com/p2"
        )
        self.order = Order.objects.create(
            user=self.user,
            customer_name="Juan Pérez",
            customer_email="juan@example.com",
            customer_phone="+34600000000",
            delivery_address="Calle Example 123",
            delivery_city="Sevilla",
            delivery_postal_code="41001",
            notes="Entregar por la mañana"
        )
    
    def test_order_creation(self):
        """Verifica que se crea correctamente un pedido."""
        self.assertIsNotNone(self.order.id)
        self.assertEqual(self.order.customer_name, "Juan Pérez")
        self.assertEqual(self.order.status, 'pending')
        self.assertEqual(self.order.user, self.user)
    
    def test_order_str_representation(self):
        """Verifica la representación string del modelo."""
        expected = f"Pedido #{self.order.id} - Juan Pérez ({self.order.created_at:%Y-%m-%d})"
        self.assertEqual(str(self.order), expected)
    
    def test_order_get_total_items_empty(self):
        """Verifica get_total_items con pedido vacío."""
        self.assertEqual(self.order.get_total_items(), 0)
    
    def test_order_get_total_items_with_items(self):
        """Verifica get_total_items con items."""
        OrderItem.objects.create(order=self.order, product=self.product1, quantity=2)
        OrderItem.objects.create(order=self.order, product=self.product2, quantity=3)
        self.assertEqual(self.order.get_total_items(), 5)
    
    def test_order_get_items_summary(self):
        """Verifica get_items_summary."""
        OrderItem.objects.create(order=self.order, product=self.product1, quantity=2)
        OrderItem.objects.create(order=self.order, product=self.product2, quantity=1)
        summary = self.order.get_items_summary()
        self.assertIn("Producto 1 (x2)", summary)
        self.assertIn("Producto 2 (x1)", summary)
    
    def test_order_ordering(self):
        """Verifica que los pedidos se ordenan por created_at descendente."""
        order2 = Order.objects.create(
            user=self.user,
            customer_name="María López",
            customer_email="maria@example.com",
            delivery_address="Calle Test",
            delivery_city="Madrid",
            delivery_postal_code="28001"
        )
        orders = Order.objects.all()
        self.assertEqual(orders[0], order2)
        self.assertEqual(orders[1], self.order)


class OrderItemModelTest(TestCase):
    """Pruebas unitarias para el modelo OrderItem."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.user = User.objects.create_user(
            username="itemuser@example.com",
            email="itemuser@example.com",
            password="TestPass123"
        )
        self.product = Product.objects.create(
            name="Test Product",
            herbalife_url="https://example.com/test"
        )
        self.order = Order.objects.create(
            user=self.user,
            customer_name="Test Customer",
            customer_email="test@example.com",
            delivery_address="Test Address",
            delivery_city="Test City",
            delivery_postal_code="12345"
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
    
    def test_order_item_creation(self):
        """Verifica que se crea correctamente un item de pedido."""
        self.assertIsNotNone(self.order_item.id)
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.quantity, 3)
    
    def test_order_item_default_quantity(self):
        """Verifica que la cantidad por defecto es 1."""
        item = OrderItem.objects.create(
            order=self.order,
            product=self.product
        )
        self.assertEqual(item.quantity, 1)
    
    def test_order_item_relationship(self):
        """Verifica la relación con Order."""
        self.assertIn(self.order_item, self.order.items.all())


# ============================================================
# TESTS DE FORMULARIOS
# ============================================================

class AppointmentFormTest(TestCase):
    """Pruebas unitarias para el formulario AppointmentForm."""
    
    def test_appointment_form_valid(self):
        """Verifica que el formulario es válido con datos correctos."""
        future_datetime = timezone.now() + timedelta(days=1)
        form_data = {
            'name': 'Juan Pérez',
            'email': 'juan@example.com',
            'datetime': future_datetime.strftime('%Y-%m-%dT%H:%M'),
            'notes': 'Primera cita'
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_appointment_form_missing_name(self):
        """Verifica que el formulario es inválido sin nombre."""
        future_datetime = timezone.now() + timedelta(days=1)
        form_data = {
            'email': 'juan@example.com',
            'datetime': future_datetime.strftime('%Y-%m-%dT%H:%M')
        }
        form = AppointmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
    
    def test_appointment_form_invalid_email(self):
        """Verifica que el formulario rechaza emails inválidos."""
        future_datetime = timezone.now() + timedelta(days=1)
        form_data = {
            'name': 'Juan Pérez',
            'email': 'email_invalido',
            'datetime': future_datetime.strftime('%Y-%m-%dT%H:%M')
        }
        form = AppointmentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class RegistrationFormTest(TestCase):
    """Pruebas unitarias para el formulario RegistrationForm."""
    
    def test_registration_form_valid(self):
        """Verifica que el formulario es válido con datos correctos."""
        form_data = {
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'juan@example.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'security_question': '¿Cuál es el nombre de tu primera mascota?',
            'security_answer': 'Rex'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_registration_form_passwords_dont_match(self):
        """Verifica que el formulario rechaza contraseñas que no coinciden."""
        form_data = {
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'juan@example.com',
            'password1': 'SecurePass123!',
            'password2': 'DifferentPass456!',
            'security_question': '¿Cuál es el nombre de tu primera mascota?',
            'security_answer': 'Rex'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
    
    def test_registration_form_duplicate_email(self):
        """Verifica que el formulario rechaza emails duplicados."""
        User.objects.create_user(
            username='existing@example.com',
            email='existing@example.com',
            password='TestPass123'
        )
        form_data = {
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'existing@example.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'security_question': '¿Cuál es el nombre de tu primera mascota?',
            'security_answer': 'Rex'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
    
    def test_registration_form_creates_security_profile(self):
        """Verifica que el formulario crea el perfil de seguridad."""
        form_data = {
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'newuser@example.com',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'security_question': '¿Cuál es el nombre de tu primera mascota?',
            'security_answer': 'Rex'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        
        self.assertTrue(SecurityProfile.objects.filter(user=user).exists())
        security_profile = SecurityProfile.objects.get(user=user)
        self.assertTrue(security_profile.check_answer('Rex'))


class LoginFormTest(TestCase):
    """Pruebas unitarias para el formulario LoginForm."""
    
    def test_login_form_password_method_valid(self):
        """Verifica que el formulario es válido con método password."""
        form_data = {
            'email': 'user@example.com',
            'login_method': 'password',
            'password': 'TestPass123'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_login_form_security_method_valid(self):
        """Verifica que el formulario es válido con método security."""
        form_data = {
            'email': 'user@example.com',
            'login_method': 'security',
            'security_answer': 'Rex'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_login_form_missing_email(self):
        """Verifica que el formulario es inválido sin email."""
        form_data = {
            'login_method': 'password',
            'password': 'TestPass123'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)


class CheckoutFormTest(TestCase):
    """Pruebas unitarias para el formulario CheckoutForm."""
    
    def test_checkout_form_valid(self):
        """Verifica que el formulario es válido con datos correctos."""
        form_data = {
            'customer_name': 'Juan Pérez',
            'customer_email': 'juan@example.com',
            'customer_phone': '+34600000000',
            'delivery_address': 'Calle Example 123',
            'delivery_city': 'Sevilla',
            'delivery_postal_code': '41001',
            'notes': 'Entregar por la mañana'
        }
        form = CheckoutForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_checkout_form_optional_fields(self):
        """Verifica que campos opcionales pueden estar vacíos."""
        form_data = {
            'customer_name': 'Juan Pérez',
            'customer_email': 'juan@example.com',
            'delivery_address': 'Calle Example 123',
            'delivery_city': 'Sevilla',
            'delivery_postal_code': '41001'
        }
        form = CheckoutForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_checkout_form_missing_required_fields(self):
        """Verifica que el formulario es inválido sin campos requeridos."""
        form_data = {
            'customer_name': 'Juan Pérez'
        }
        form = CheckoutForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('customer_email', form.errors)
        self.assertIn('delivery_address', form.errors)


# ============================================================
# TESTS DEL CARRITO
# ============================================================

class CartTest(TestCase):
    """Pruebas unitarias para la clase Cart."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        from django.test import RequestFactory
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        from django.contrib.sessions.middleware import SessionMiddleware
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(self.request)
        self.request.session.save()
        
        self.product1 = Product.objects.create(
            name="Producto 1",
            herbalife_url="https://example.com/p1",
            image_url="https://example.com/img1.jpg"
        )
        self.product2 = Product.objects.create(
            name="Producto 2",
            herbalife_url="https://example.com/p2"
        )
        self.cart = Cart(self.request)
    
    def test_cart_initialization(self):
        """Verifica que el carrito se inicializa correctamente."""
        self.assertIsNotNone(self.cart.cart)
        self.assertEqual(len(self.cart.cart), 0)
    
    def test_cart_add_product(self):
        """Verifica que se puede añadir un producto al carrito."""
        self.cart.add(self.product1, quantity=2)
        self.assertIn(str(self.product1.id), self.cart.cart)
        self.assertEqual(self.cart.cart[str(self.product1.id)]['quantity'], 2)
    
    def test_cart_add_existing_product(self):
        """Verifica que añadir un producto existente incrementa la cantidad."""
        self.cart.add(self.product1, quantity=1)
        self.cart.add(self.product1, quantity=2)
        self.assertEqual(self.cart.cart[str(self.product1.id)]['quantity'], 3)
    
    def test_cart_update_quantity(self):
        """Verifica que se puede actualizar la cantidad de un producto."""
        self.cart.add(self.product1, quantity=1)
        self.cart.add(self.product1, quantity=5, update_quantity=True)
        self.assertEqual(self.cart.cart[str(self.product1.id)]['quantity'], 5)
    
    def test_cart_remove_product(self):
        """Verifica que se puede eliminar un producto del carrito."""
        self.cart.add(self.product1, quantity=2)
        self.cart.remove(self.product1)
        self.assertNotIn(str(self.product1.id), self.cart.cart)
    
    def test_cart_clear(self):
        """Verifica que se puede vaciar el carrito."""
        self.cart.add(self.product1, quantity=2)
        self.cart.add(self.product2, quantity=1)
        self.cart.clear()
        # Después de clear(), el carrito se elimina de la sesión
        self.assertNotIn('cart', self.request.session)
    
    def test_cart_iteration(self):
        """Verifica que se puede iterar sobre el carrito."""
        self.cart.add(self.product1, quantity=2)
        self.cart.add(self.product2, quantity=1)
        items = list(self.cart)
        self.assertEqual(len(items), 2)
    
    def test_cart_len(self):
        """Verifica que len() retorna el número total de items."""
        self.cart.add(self.product1, quantity=2)
        self.cart.add(self.product2, quantity=3)
        self.assertEqual(len(self.cart), 5)


# ============================================================
# TESTS DE FUNCIONES DE UTILIDAD
# ============================================================

class SendSMSTest(TestCase):
    """Pruebas unitarias para la función send_price_sms."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.user = User.objects.create_user(
            username="smsuser@example.com",
            email="smsuser@example.com",
            password="TestPass123"
        )
        self.order = Order.objects.create(
            user=self.user,
            customer_name="Juan Pérez",
            customer_email="juan@example.com",
            customer_phone="+34600000000",
            delivery_address="Calle Test",
            delivery_city="Sevilla",
            delivery_postal_code="41001"
        )
    
    @patch('home.send_sms.Client')
    def test_send_price_sms_success(self, mock_twilio_client):
        """Verifica que send_price_sms envía SMS correctamente."""
        from home.send_sms import send_price_sms
        
        # Mock del cliente Twilio
        mock_instance = MagicMock()
        mock_twilio_client.return_value = mock_instance
        mock_message = MagicMock()
        mock_message.sid = 'SM123456789'
        mock_instance.messages.create.return_value = mock_message
        
        result = send_price_sms(self.order, 45.99)
        
        self.assertTrue(result)
        mock_instance.messages.create.assert_called_once()
    
    @patch('home.send_sms.Client')
    def test_send_price_sms_failure(self, mock_twilio_client):
        """Verifica que send_price_sms maneja errores correctamente."""
        from home.send_sms import send_price_sms
        
        # Mock que lanza excepción
        mock_instance = MagicMock()
        mock_twilio_client.return_value = mock_instance
        mock_instance.messages.create.side_effect = Exception("Twilio error")
        
        result = send_price_sms(self.order, 45.99)
        
        self.assertFalse(result)


class SendEmailTest(TestCase):
    """Pruebas unitarias para la función send_daily_order_summary."""
    
    def setUp(self):
        """Configuración inicial para cada test."""
        self.user = User.objects.create_user(
            username="emailuser@example.com",
            email="emailuser@example.com",
            password="TestPass123"
        )
        self.product = Product.objects.create(
            name="Test Product",
            herbalife_url="https://example.com/test"
        )
    
    @patch('home.send_mail.EmailMessage')
    def test_send_daily_order_summary_with_orders(self, mock_email):
        """Verifica que se envía el email con pedidos."""
        from home.send_mail import send_daily_order_summary
        
        # Crear pedido de hoy
        order = Order.objects.create(
            user=self.user,
            customer_name="Juan Pérez",
            customer_email="juan@example.com",
            delivery_address="Calle Test",
            delivery_city="Sevilla",
            delivery_postal_code="41001"
        )
        OrderItem.objects.create(order=order, product=self.product, quantity=2)
        
        # Mock del EmailMessage
        mock_instance = MagicMock()
        mock_email.return_value = mock_instance
        
        result = send_daily_order_summary()
        
        mock_instance.send.assert_called_once()
        self.assertIn("1 pedidos", result)
    
    @patch('home.send_mail.EmailMessage')
    def test_send_daily_order_summary_no_orders(self, mock_email):
        """Verifica que se envía el email sin pedidos."""
        from home.send_mail import send_daily_order_summary
        
        # Mock del EmailMessage
        mock_instance = MagicMock()
        mock_email.return_value = mock_instance
        
        result = send_daily_order_summary()
        
        mock_instance.send.assert_called_once()
        self.assertIn("0 pedidos", result)
