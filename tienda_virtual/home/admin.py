from django.contrib import admin
from .models import Appointment

from .models import SecurityProfile


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

