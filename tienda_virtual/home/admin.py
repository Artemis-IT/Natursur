from django.contrib import admin
from .models import Appointment, SecurityProfile, Product


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'datetime', 'created_at')
	list_filter = ('datetime',)
	search_fields = ('name', 'email')


@admin.register(SecurityProfile)
class SecurityProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'question', 'has_answer')
	search_fields = ('user__username', 'user__email', 'question')

	def has_answer(self, obj):
		return bool(obj.answer)
	has_answer.boolean = True
	has_answer.short_description = 'Respuesta guardada'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'is_active', 'created_at', 'updated_at')
	list_filter = ('is_active', 'category', 'created_at')
	search_fields = ('name', 'description')
	list_editable = ('is_active',)
	readonly_fields = ('created_at', 'updated_at')
	fieldsets = (
		('Información del producto', {
			'fields': ('name', 'herbalife_url', 'category', 'description')
		}),
		('Imagen', {
			'fields': ('image_url',)
		}),
		('Estado', {
			'fields': ('is_active', 'created_at', 'updated_at')
		}),
	)

