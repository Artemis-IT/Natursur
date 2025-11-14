from django.db import models

# Create your models here.


class Appointment(models.Model):
	"""Modelo para almacenar citas/agendamientos."""
	name = models.CharField(max_length=120)
	email = models.EmailField()
	datetime = models.DateTimeField()
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-datetime']

	def __str__(self):
		return f"{self.name} — {self.datetime:%Y-%m-%d %H:%M}"


from django.conf import settings


class SecurityProfile(models.Model):
	"""Guarda la pregunta y respuesta de seguridad asociada a un usuario."""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='security_profile')
	question = models.CharField(max_length=255)
	answer = models.CharField(max_length=255)

	def __str__(self):
		return f"Security for {self.user.get_username()}"

	def check_answer(self, raw_answer):
		"""Comprueba la respuesta contra el hash almacenado."""
		from django.contrib.auth.hashers import check_password
		return check_password(raw_answer, self.answer)


class Product(models.Model):
	"""Modelo para productos de Herbalife obtenidos mediante scraping."""
	name = models.CharField(max_length=255)
	herbalife_url = models.URLField(max_length=500, unique=True)
	image_url = models.URLField(max_length=500, blank=True, null=True)
	description = models.TextField(blank=True)
	category = models.CharField(max_length=100, blank=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']
		verbose_name = 'Producto Herbalife'
		verbose_name_plural = 'Productos Herbalife'

	def __str__(self):
		return self.name

class Order(models.Model):
	"""Modelo para almacenar pedidos realizados por clientes."""
	STATUS_CHOICES = [
		('pending', 'Pendiente'),
		('processing', 'En proceso'),
		('completed', 'Completado'),
		('cancelled', 'Cancelado'),
	]
	
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
	customer_name = models.CharField(max_length=200)
	customer_email = models.EmailField()
	customer_phone = models.CharField(max_length=20, blank=True)
	delivery_address = models.TextField()
	delivery_city = models.CharField(max_length=100)
	delivery_postal_code = models.CharField(max_length=10)
	notes = models.TextField(blank=True, help_text='Notas o instrucciones especiales para el pedido')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'
	
	def __str__(self):
		return f"Pedido #{self.id} - {self.customer_name} ({self.created_at:%Y-%m-%d})"
	
	def get_total_items(self):
		"""Retorna el número total de productos en el pedido."""
		return sum(item.quantity for item in self.items.all())
	
	def get_items_summary(self):
		"""Retorna un resumen de los items del pedido."""
		return ", ".join([f"{item.product.name} (x{item.quantity})" for item in self.items.all()[:3]])


class OrderItem(models.Model):
	"""Modelo para los items individuales de un pedido."""
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	product_name = models.CharField(max_length=255)
	product_url = models.URLField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name = 'Item de Pedido'
		verbose_name_plural = 'Items de Pedido'
	
	def __str__(self):
		return f"{self.quantity}x {self.product_name}"
	
	def save(self, *args, **kwargs):
     
		if not self.product_name:
			self.product_name = self.product.name
		if not self.product_url:
			self.product_url = self.product.herbalife_url
		super().save(*args, **kwargs)
