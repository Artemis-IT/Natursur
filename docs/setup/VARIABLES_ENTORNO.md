# Variables de Entorno - Guía Completa

## Descripción

Este documento lista todas las variables de entorno necesarias para el correcto funcionamiento del proyecto Natursur en diferentes entornos (desarrollo, producción).

## Archivo `.env`

Crear un archivo `.env` en la raíz del proyecto (mismo nivel que `requirements.txt`) con el siguiente contenido:

```env
# ============================================================
# CONFIGURACIÓN GENERAL DE DJANGO
# ============================================================

# Clave secreta de Django (generar una única para producción)
SECRET_KEY=django-insecure-CAMBIAR-ESTA-CLAVE-EN-PRODUCCION

# Modo debug (True para desarrollo, False para producción)
DEBUG=True

# Hosts permitidos (separados por comas)
ALLOWED_HOSTS=localhost,127.0.0.1


# ============================================================
# BASE DE DATOS (DESARROLLO LOCAL)
# ============================================================

# PostgreSQL Local (si usas PostgreSQL en desarrollo)
DATABASE_NAME=tienda_virtual
DATABASE_USER=postgres
DATABASE_PASSWORD=tu_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# NOTA: Si usas SQLite en desarrollo, no necesitas estas variables
# Django usará automáticamente db.sqlite3


# ============================================================
# BASE DE DATOS (PRODUCCIÓN RENDER)
# ============================================================

# Esta variable la proporciona automáticamente Render
# No la configures manualmente en desarrollo
# DATABASE_URL=postgres://user:password@host:port/database


# ============================================================
# CONFIGURACIÓN DE EMAIL (SMTP)
# ============================================================

# Backend de email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend

# Servidor SMTP (Gmail por defecto)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Credenciales de email
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_de_aplicacion_aqui

# NOTA: Para Gmail, debes generar una "Contraseña de Aplicación"
# Ver: docs/setup/EMAIL_CONFIGURACION.md


# ============================================================
# CONFIGURACIÓN DE TWILIO (SMS)
# ============================================================

# Credenciales de Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=tu_auth_token_aqui
TWILIO_PHONE_NUMBER=+34XXXXXXXXX

# NOTA: Obtener desde https://console.twilio.com/
# Ver: docs/setup/TWILIO_CONFIGURACION.md


# ============================================================
# CONFIGURACIÓN ADICIONAL (OPCIONAL)
# ============================================================

# Versión de Python (para Render)
PYTHON_VERSION=3.11.0
```

## Variables por Categoría

### 🔐 Seguridad

| Variable | Obligatoria | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `SECRET_KEY` | ✅ Sí | Clave secreta de Django | `django-insecure-...` |
| `DEBUG` | ✅ Sí | Modo debug (False en producción) | `True` / `False` |
| `ALLOWED_HOSTS` | ✅ Sí | Hosts permitidos | `localhost,127.0.0.1` |

**Generar SECRET_KEY segura:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 🗄️ Base de Datos (Desarrollo Local)

| Variable | Obligatoria | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `DATABASE_NAME` | ⚠️ Condicional* | Nombre de la base de datos | `tienda_virtual` |
| `DATABASE_USER` | ⚠️ Condicional* | Usuario de PostgreSQL | `postgres` |
| `DATABASE_PASSWORD` | ⚠️ Condicional* | Contraseña de PostgreSQL | `mypassword` |
| `DATABASE_HOST` | ⚠️ Condicional* | Host de PostgreSQL | `localhost` |
| `DATABASE_PORT` | ⚠️ Condicional* | Puerto de PostgreSQL | `5432` |

**\*Condicional:** Solo si usas PostgreSQL en desarrollo. Si usas SQLite, no son necesarias.

### 🗄️ Base de Datos (Producción)

| Variable | Obligatoria | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `DATABASE_URL` | ✅ En producción | URL completa de conexión | `postgres://user:pass@host/db` |

**NOTA:** Esta variable la proporciona automáticamente Render. No la configures en `.env` local.

### 📧 Email (SMTP)

| Variable | Obligatoria | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `EMAIL_BACKEND` | ❌ No | Backend de email | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST` | ✅ Sí | Servidor SMTP | `smtp.gmail.com` |
| `EMAIL_PORT` | ❌ No | Puerto SMTP | `587` |
| `EMAIL_USE_TLS` | ❌ No | Usar TLS | `True` |
| `EMAIL_HOST_USER` | ✅ Sí | Email del remitente | `miapp@gmail.com` |
| `EMAIL_HOST_PASSWORD` | ✅ Sí | Contraseña de aplicación | `abcd efgh ijkl mnop` |

**IMPORTANTE:** Para Gmail, usa una [Contraseña de Aplicación](https://support.google.com/accounts/answer/185833), no tu contraseña normal.

### 📱 Twilio (SMS)

| Variable | Obligatoria | Descripción | Ejemplo |
|----------|------------|-------------|---------|
| `TWILIO_ACCOUNT_SID` | ✅ Sí | Account SID de Twilio | `ACxxxxxxxxxxxxxxxx` |
| `TWILIO_AUTH_TOKEN` | ✅ Sí | Auth Token de Twilio | `your_auth_token` |
| `TWILIO_PHONE_NUMBER` | ✅ Sí | Número de teléfono Twilio | `+34600000000` |

**Obtener credenciales:** [Twilio Console](https://console.twilio.com/)

## Configuración por Entorno

### 🏠 Desarrollo Local

Archivo `.env` mínimo necesario:

```env
# Django
SECRET_KEY=django-insecure-desarrollo-clave
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Email
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_aplicacion

# Twilio (opcional en desarrollo)
TWILIO_ACCOUNT_SID=ACxxx...
TWILIO_AUTH_TOKEN=xxx...
TWILIO_PHONE_NUMBER=+34xxx...
```

### 🌐 Producción (Render)

Variables a configurar en Render Dashboard:

```env
# Django
SECRET_KEY=generar-una-clave-segura-unica
DEBUG=False
ALLOWED_HOSTS=.onrender.com,tudominio.com
PYTHON_VERSION=3.11.0

# Database (automática)
DATABASE_URL=[proporcionada por Render]

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=contraseña_aplicacion

# Twilio
TWILIO_ACCOUNT_SID=ACxxx...
TWILIO_AUTH_TOKEN=xxx...
TWILIO_PHONE_NUMBER=+34xxx...
```

## Validación de Variables

Para verificar que todas las variables están configuradas correctamente, ejecutar:

```python
# En Django shell: python manage.py shell
from django.conf import settings
import os

# Verificar variables críticas
print("DEBUG:", settings.DEBUG)
print("SECRET_KEY configurada:", bool(settings.SECRET_KEY))
print("EMAIL_HOST_USER:", settings.EMAIL_HOST_USER)
print("TWILIO_ACCOUNT_SID:", settings.TWILIO_ACCOUNT_SID[:10] + "...")
print("DATABASE:", settings.DATABASES['default']['ENGINE'])
```

## Seguridad

### ⚠️ IMPORTANTE: Proteger Credenciales

**✅ HACER:**
- Usar archivo `.env` en desarrollo
- Añadir `.env` a `.gitignore`
- Usar variables de entorno en Render
- Generar SECRET_KEY única para producción
- Usar contraseñas de aplicación (no contraseñas normales)

**❌ NO HACER:**
- Commitear `.env` al repositorio
- Hardcodear credenciales en el código
- Compartir credenciales en Slack/email
- Usar la misma SECRET_KEY en dev y prod
- Usar contraseñas de cuentas personales

### `.gitignore`

Asegurarse que `.gitignore` incluye:

```gitignore
# Variables de entorno
.env
.env.local
.env.production

# Base de datos
db.sqlite3
*.db
```

## Troubleshooting

### Error: "SECRET_KEY is not set"
**Solución:** Verificar que `.env` existe y contiene `SECRET_KEY=...`

### Error: "EMAIL_HOST_USER is not set"
**Solución:** Añadir `EMAIL_HOST_USER` al archivo `.env` o variables de Render

### SMS no funciona
**Solución:** Verificar que todas las variables `TWILIO_*` estén configuradas correctamente

### Base de datos no conecta en producción
**Solución:** Verificar que `DATABASE_URL` esté configurada (automática en Render)

## Scripts de Ayuda

### Generar SECRET_KEY

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Probar Email

```bash
python tienda_virtual/run_daily_task.py
```

### Verificar Variables

```bash
python manage.py shell
>>> from django.conf import settings
>>> print(settings.DATABASES)
```

## Referencias

- [Django Settings](https://docs.djangoproject.com/en/5.2/topics/settings/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [12 Factor App](https://12factor.net/config)
- [Render Environment Variables](https://render.com/docs/environment-variables)

---

**Última actualización:** Noviembre 2025  
**Responsable:** Equipo Artemis IT
