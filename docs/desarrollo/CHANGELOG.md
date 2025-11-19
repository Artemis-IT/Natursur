# Nuevas Funcionalidades - Changelog

## Versión 1.0 - Noviembre 2025

### 🆕 Funcionalidades Añadidas

#### 1. Sistema de Notificaciones SMS (Twilio)

**Descripción:** Integración con Twilio para enviar SMS automáticos a clientes al realizar pedidos.

**Características:**
- Envío automático al confirmar pedido
- Información del precio total
- Instrucciones de pago vía Bizum
- Número de referencia del pedido

**Archivos involucrados:**
- `tienda_virtual/home/send_sms.py` - Lógica de envío
- `tienda_virtual/tienda_virtual/settings.py` - Configuración de Twilio

**Variables de entorno requeridas:**
```env
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=...
```

**Documentación:** [TWILIO_CONFIGURACION.md](../setup/TWILIO_CONFIGURACION.md)

---

#### 2. Resumen Diario de Pedidos por Email

**Descripción:** Sistema automático que envía un resumen diario de todos los pedidos recibidos a los administradores.

**Características:**
- Email diario con todos los pedidos del día
- Información detallada de cada pedido (artículos, cliente, dirección)
- Formato legible y estructurado
- Si no hay pedidos, envía notificación de "Sin pedidos"

**Archivos involucrados:**
- `tienda_virtual/home/send_mail.py` - Lógica de generación y envío
- `tienda_virtual/run_daily_task.py` - Script para ejecución programada
- `tienda_virtual/tienda_virtual/settings.py` - Configuración SMTP

**Variables de entorno requeridas:**
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
```

**Ejecución:**
```bash
# Manual
python tienda_virtual/run_daily_task.py

# Automática (configurar en cron/tareas programadas)
59 23 * * * cd /ruta/proyecto/tienda_virtual && python run_daily_task.py
```

**Documentación:** [EMAIL_CONFIGURACION.md](../setup/EMAIL_CONFIGURACION.md)

---

#### 3. Despliegue en Render (Cloud)

**Descripción:** Configuración completa para desplegar la aplicación en Render, plataforma cloud con plan gratuito.

**Características:**
- Despliegue automático desde GitHub
- Base de datos PostgreSQL gestionada
- Configuración de variables de entorno
- Servicio de archivos estáticos con WhiteNoise
- HTTPS automático
- Dominio gratuito .onrender.com

**Archivos involucrados:**
- `render.yaml` - Configuración de Blueprint para Render
- `requirements.txt` - Dependencias necesarias (gunicorn, whitenoise, dj-database-url)
- `tienda_virtual/tienda_virtual/settings.py` - Configuración para producción

**Características del Blueprint:**
```yaml
- Web Service (Python)
- PostgreSQL Database
- Migraciones automáticas
- Collectstatic automático
- Variables de entorno seguras
```

**Documentación:** [RENDER_DESPLIEGUE.md](../setup/RENDER_DESPLIEGUE.md)

---

#### 4. Gestión de Archivos Estáticos con WhiteNoise

**Descripción:** Integración de WhiteNoise para servir archivos estáticos eficientemente en producción.

**Características:**
- Compresión automática de archivos estáticos
- Caché optimizado
- Sin necesidad de CDN separado
- Compatible con Render y otros hosts

**Configuración en `settings.py`:**
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Añadido
    # ... otros middlewares
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

#### 5. Configuración de Base de Datos Dual

**Descripción:** Soporte para SQLite (desarrollo) y PostgreSQL (producción) con cambio automático.

**Características:**
- SQLite para desarrollo local
- PostgreSQL para producción (Render)
- Cambio automático basado en variable `DATABASE_URL`
- Migraciones compatibles con ambas

**Código en `settings.py`:**
```python
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            # ... configuración PostgreSQL local
        }
    }
```

---

### 🔧 Mejoras Técnicas

#### Variables de Entorno con python-dotenv

**Añadido:** Soporte para archivo `.env` usando python-dotenv

**Beneficios:**
- Separación de configuración sensible del código
- Fácil cambio entre entornos
- Seguridad mejorada (no commitear credenciales)

**Ejemplo `.env`:**
```env
# Database
DATABASE_NAME=tienda_virtual
DATABASE_USER=postgres
DATABASE_PASSWORD=password

# Email
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=app_password

# Twilio
TWILIO_ACCOUNT_SID=ACxxxx
TWILIO_AUTH_TOKEN=token
TWILIO_PHONE_NUMBER=+34600000000

# Django
SECRET_KEY=your-secret-key
DEBUG=True
```

---

#### Dependencias Actualizadas

**Nuevas dependencias añadidas a `requirements.txt`:**

```
# Servidor WSGI para producción
gunicorn==21.2.0

# Archivos estáticos
whitenoise==6.6.0

# Base de datos
dj-database-url==2.1.0
psycopg2-binary==2.9.9

# Variables de entorno
python-dotenv==1.0.0

# Notificaciones
twilio==8.10.0
```

---

### 📋 Checklist de Migración

Si ya tienes el proyecto desplegado localmente, para añadir estas funcionalidades:

- [ ] Actualizar `requirements.txt` e instalar nuevas dependencias
- [ ] Añadir variables de entorno en `.env`
- [ ] Configurar cuenta de Twilio
- [ ] Configurar contraseña de aplicación de Gmail
- [ ] Probar envío de SMS localmente
- [ ] Probar envío de email localmente
- [ ] Configurar tarea programada para email diario
- [ ] Crear cuenta en Render
- [ ] Configurar Blueprint en Render
- [ ] Añadir variables de entorno en Render
- [ ] Desplegar y verificar funcionamiento

---

### 🐛 Problemas Conocidos y Soluciones

#### SMS no se envía
- **Causa:** Número no verificado en cuenta Twilio de prueba
- **Solución:** Verificar el número en Twilio Console

#### Email no llega
- **Causa:** Contraseña de aplicación incorrecta
- **Solución:** Generar nueva contraseña de aplicación en Google

#### Render suspende el servicio
- **Causa:** Plan gratuito suspende tras 15 minutos de inactividad
- **Solución:** Considerar actualizar a plan de pago o aceptar el delay inicial

---

### 🔮 Próximas Funcionalidades Planificadas

- [ ] Sistema de notificaciones push
- [ ] Panel de estadísticas de pedidos
- [ ] Exportación de reportes a PDF
- [ ] API REST para integración con apps móviles
- [ ] Sistema de cupones y descuentos
- [ ] Multi-idioma (i18n)

---

### 📚 Referencias

- [Documentación Twilio](https://www.twilio.com/docs)
- [Documentación Django Email](https://docs.djangoproject.com/en/5.2/topics/email/)
- [Documentación Render](https://render.com/docs)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)

---

**Fecha de última actualización:** Noviembre 2025  
**Versión:** 1.0.0  
**Responsable:** Equipo Artemis IT
