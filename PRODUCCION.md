# 🔧 Configuración para Producción

**Elaborado por:** Antonio Luis Jiménez de la Fuente (Project Manager) y el Equipo de Proyecto Natursur.  
**Tech Lead (desarrollo web):** Alejandro Vela Molina.

## Cambios necesarios antes de desplegar

### 1. settings.py - Seguridad

En `tienda_virtual/tienda_virtual/settings.py`, cambiar:

```python
# ❌ ANTES (Desarrollo)
DEBUG = True
SECRET_KEY = 'django-insecure-...'
ALLOWED_HOSTS = []

# ✅ DESPUÉS (Producción)
DEBUG = False
SECRET_KEY = 'una-clave-super-segura-y-aleatoria-de-50-caracteres'
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com', '192.168.1.100']
```

Generar SECRET_KEY segura:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Base de Datos - PostgreSQL

Para producción, usar PostgreSQL en lugar de SQLite:

```bash
# Instalar driver PostgreSQL
pip install psycopg2-binary
```

En `settings.py`:
```python
# SQLite (Desarrollo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PostgreSQL (Producción)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'natursur_db',
        'USER': 'natursur_user',
        'PASSWORD': 'contraseña-super-segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. HTTPS y Cookies Seguras

En `settings.py`:
```python
# Forzar HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 año
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
```

### 4. Archivos Estáticos

```python
# En settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Ejecutar:
```bash
python manage.py collectstatic --noinput
```

### 5. Logs y Monitoreo

```python
# En settings.py - Agregar logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/natursur.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

---

## 🚀 Opciones de Despliegue

### Opción 1: Heroku (Más Fácil)

```bash
# 1. Instalar Heroku CLI
# 2. Login
heroku login

# 3. Crear app
heroku create natursur-app

# 4. Agregar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 5. Pushear código
git push heroku main

# 6. Migrar
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Opción 2: DigitalOcean / Linode (Tradicional)

```bash
# En servidor Linux

# 1. Instalar dependencias
sudo apt-get update
sudo apt-get install python3-pip python3-venv postgresql nginx supervisor

# 2. Clonar repo
git clone https://github.com/alevelmol/Proyecto-PGPI.git
cd Proyecto-PGPI

# 3. Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# 4. Migrar
python manage.py migrate
python manage.py collectstatic --noinput

# 5. Configurar Gunicorn (supervisor o systemd)
# 6. Configurar Nginx como reverse proxy
```

### Opción 3: PythonAnywhere (Más Fácil)

- Registrarse en www.pythonanywhere.com
- Subir archivos vía Git
- Configurar a través del dashboard
- Datos gratuitos con SQLite limitado

---

## 📋 Checklist Pre-Producción

- [ ] DEBUG = False
- [ ] SECRET_KEY cambiada y segura
- [ ] ALLOWED_HOSTS configurado
- [ ] Base de datos PostgreSQL (no SQLite)
- [ ] HTTPS habilitado (SECURE_SSL_REDIRECT = True)
- [ ] Cookies seguras (SESSION_COOKIE_SECURE = True)
- [ ] Archivos estáticos recopilados (collectstatic)
- [ ] Servidor web configurado (Nginx, Apache)
- [ ] Logs configurados
- [ ] Backups automáticos habilitados
- [ ] Monitor de uptime configurado (Uptime Robot, New Relic)
- [ ] Firewall configurado
- [ ] Email SMTP configurado para notificaciones

---

## 🔍 Monitoreo en Producción

```bash
# Ver logs en tiempo real
tail -f /var/log/django/natursur.log

# Revisar BD
python manage.py dbshell

# Backup BD
pg_dump natursur_db > backup-$(date +%Y-%m-%d).sql

# Restore DB
psql natursur_db < backup-2024-01-01.sql
```

---

## 📈 Performance

- Usar CDN para archivos estáticos (CloudFlare, AWS CloudFront)
- Cache con Redis/Memcached
- Comprimir CSS y JS
- Optimizar imágenes
- Usar django-extensions para profiling

```bash
pip install django-extensions django-debug-toolbar
```

---

¡Tu aplicación está lista para producción! 🚀
