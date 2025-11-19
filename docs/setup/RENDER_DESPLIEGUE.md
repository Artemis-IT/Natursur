# Despliegue en Render

## Descripción

Render es una plataforma de cloud hosting que permite desplegar aplicaciones web de forma sencilla. Este proyecto está configurado para desplegarse automáticamente en Render usando el archivo `render.yaml`.

## Requisitos Previos

1. Cuenta en [Render](https://render.com/) (gratuita)
2. Repositorio del proyecto en GitHub
3. Base de datos PostgreSQL (proporcionada por Render)

## Configuración Inicial

### 1. Conectar Repositorio

1. Acceder a [Render Dashboard](https://dashboard.render.com/)
2. Click en "New +" → "Blueprint"
3. Conectar cuenta de GitHub
4. Seleccionar el repositorio del proyecto

### 2. Configuración del Blueprint

Render detectará automáticamente el archivo `render.yaml` que contiene:

```yaml
services:
  - type: web
    name: tienda-virtual
    runtime: python
    plan: free
    rootDir: tienda_virtual
    buildCommand: pip install -r ../requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
    startCommand: gunicorn tienda_virtual.wsgi:application
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: tienda-virtual-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: DEBUG
        value: False
      - key: ALLOWED_HOSTS
        value: .onrender.com,localhost,127.0.0.1

databases:
  - name: tienda-virtual-db
    databaseName: tienda_virtual
    user: tienda_virtual_user
    plan: free
```

### 3. Variables de Entorno Adicionales

Añadir manualmente las siguientes variables en Render Dashboard:

**Email Configuration:**
- `EMAIL_BACKEND`: `django.core.mail.backends.smtp.EmailBackend`
- `EMAIL_HOST`: `smtp.gmail.com`
- `EMAIL_PORT`: `587`
- `EMAIL_USE_TLS`: `True`
- `EMAIL_HOST_USER`: Tu email de Gmail
- `EMAIL_HOST_PASSWORD`: Contraseña de aplicación de Gmail

**Twilio Configuration:**
- `TWILIO_ACCOUNT_SID`: Tu Account SID de Twilio
- `TWILIO_AUTH_TOKEN`: Tu Auth Token de Twilio
- `TWILIO_PHONE_NUMBER`: Tu número de Twilio con formato `+34XXXXXXXXX`

### 4. Configurar Variables en Render

1. En el Dashboard de Render, ir al servicio `tienda-virtual`
2. Navegar a "Environment"
3. Click en "Add Environment Variable"
4. Añadir cada variable una por una
5. Guardar cambios

## Proceso de Despliegue

### Despliegue Automático

Render desplegará automáticamente cuando:
- Se hace push a la rama principal (`main`)
- Se detectan cambios en el repositorio conectado

### Despliegue Manual

1. Acceder al Dashboard de Render
2. Seleccionar el servicio `tienda-virtual`
3. Click en "Manual Deploy" → "Deploy latest commit"

### Proceso de Build

El proceso de build ejecuta automáticamente:

1. **Instalación de dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Recopilación de archivos estáticos:**
   ```bash
   python manage.py collectstatic --no-input
   ```

3. **Migraciones de base de datos:**
   ```bash
   python manage.py migrate
   ```

4. **Inicio del servidor:**
   ```bash
   gunicorn tienda_virtual.wsgi:application
   ```

## Gestión de la Base de Datos

### Acceso a la Base de Datos

Render proporciona una base de datos PostgreSQL gratuita con:
- **Conexión automática** mediante `DATABASE_URL`
- **Backups limitados** en plan gratuito
- **1 GB de almacenamiento**

### Ejecutar Migraciones Manualmente

Si es necesario ejecutar migraciones adicionales:

1. Ir al servicio en Render Dashboard
2. Click en "Shell" en el menú lateral
3. Ejecutar:
   ```bash
   python manage.py migrate
   ```

### Cargar Datos Iniciales

Para cargar fixtures o datos iniciales:

```bash
python manage.py loaddata home/fixtures/initial_data.json
```

## Archivos Estáticos

### Configuración con WhiteNoise

El proyecto usa WhiteNoise para servir archivos estáticos:

- Configurado en `settings.py`
- Los archivos se recopilan en `staticfiles/`
- Se sirven automáticamente en producción

### Verificar Archivos Estáticos

Si los archivos estáticos no se cargan:

1. Verificar que `STATIC_ROOT` esté configurado
2. Ejecutar manualmente en Shell de Render:
   ```bash
   python manage.py collectstatic --no-input
   ```

## Monitoreo y Logs

### Ver Logs en Tiempo Real

1. Acceder al servicio en Render Dashboard
2. Click en "Logs" en el menú lateral
3. Ver logs en tiempo real del servidor

### Tipos de Logs

- **Build logs:** Proceso de instalación y configuración
- **Runtime logs:** Ejecución del servidor y errores
- **Deploy logs:** Historial de despliegues

## Dominios Personalizados

### Dominio Gratuito de Render

Render proporciona automáticamente un dominio:
```
https://tienda-virtual.onrender.com
```

### Añadir Dominio Personalizado

1. En el servicio, ir a "Settings" → "Custom Domain"
2. Añadir el dominio deseado
3. Configurar los registros DNS según instrucciones de Render
4. Actualizar `ALLOWED_HOSTS` en las variables de entorno

## Limitaciones del Plan Gratuito

- **Suspensión por inactividad:** El servicio se suspende tras 15 minutos de inactividad
- **Tiempo de activación:** ~30-60 segundos para reactivarse
- **Ancho de banda:** 100 GB/mes
- **Horas de ejecución:** 750 horas/mes

## Actualización a Plan de Pago

Para producción real, se recomienda:

1. **Plan Starter ($7/mes):**
   - Sin suspensión por inactividad
   - Más recursos de CPU/RAM
   - Soporte prioritario

2. **Base de datos PostgreSQL ($7/mes):**
   - 10 GB de almacenamiento
   - Backups automáticos diarios
   - Alta disponibilidad

## Comandos Útiles en Shell

```bash
# Ver versión de Python
python --version

# Listar paquetes instalados
pip list

# Crear superusuario
python manage.py createsuperuser

# Ejecutar shell de Django
python manage.py shell

# Ver estado de migraciones
python manage.py showmigrations
```

## Resolución de Problemas

### Error: "Application failed to start"
1. Revisar los Build Logs para errores de instalación
2. Verificar que `requirements.txt` sea correcto
3. Comprobar que `gunicorn` esté en requirements.txt

### Error 500 en producción
1. Revisar Runtime Logs
2. Verificar variables de entorno
3. Comprobar que `DEBUG=False`
4. Verificar `ALLOWED_HOSTS`

### Base de datos no conecta
1. Verificar que `DATABASE_URL` esté configurada
2. Comprobar que el servicio de base de datos esté activo
3. Revisar que `dj-database-url` esté instalado

### Archivos estáticos no cargan
1. Verificar que WhiteNoise esté en `MIDDLEWARE`
2. Ejecutar `collectstatic` manualmente
3. Comprobar configuración de `STATIC_ROOT` y `STATIC_URL`

## Seguridad en Producción

### Variables Sensibles
- ✅ Usar variables de entorno para credenciales
- ✅ No commitear `.env` al repositorio
- ✅ Generar `SECRET_KEY` única para producción

### HTTPS
- ✅ Render proporciona SSL/HTTPS automáticamente
- ✅ Configurar `SECURE_SSL_REDIRECT=True` en producción

### Debug Mode
- ✅ Siempre mantener `DEBUG=False` en producción
- ✅ Configurar `ALLOWED_HOSTS` correctamente

## Referencias

- [Documentación de Render](https://render.com/docs)
- [Deploy Django on Render](https://render.com/docs/deploy-django)
- [Blueprint Specification](https://render.com/docs/blueprint-spec)
- [Environment Variables](https://render.com/docs/environment-variables)
