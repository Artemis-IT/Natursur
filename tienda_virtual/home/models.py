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

