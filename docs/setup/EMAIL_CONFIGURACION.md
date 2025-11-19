# Configuración de Envío de Emails

## Descripción

El sistema envía un resumen diario de todos los pedidos recibidos a los administradores del negocio. Este email se genera automáticamente y contiene información detallada de cada pedido del día.

## Variables de Entorno Necesarias

Añadir las siguientes variables al archivo `.env`:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_contraseña_aplicacion
```

## Configuración con Gmail

### 1. Habilitar Contraseña de Aplicación

Gmail requiere una "Contraseña de Aplicación" para permitir el acceso desde aplicaciones externas:

1. Acceder a [Cuenta de Google](https://myaccount.google.com/)
2. Ir a "Seguridad"
3. Activar la "Verificación en dos pasos" (si no está activada)
4. Buscar "Contraseñas de aplicaciones"
5. Seleccionar "Aplicación: Correo" y "Dispositivo: Otro (nombre personalizado)"
6. Copiar la contraseña de 16 caracteres generada
7. Usar esta contraseña en `EMAIL_HOST_PASSWORD`

### 2. Verificar Configuración

Para probar el envío de emails, ejecutar:

```bash
python tienda_virtual/run_daily_task.py
```

## Funcionalidad

### Resumen Diario de Pedidos

El sistema genera un email diario con:

- **Total de pedidos** recibidos en el día
- Para cada pedido:
  - Número de seguimiento
  - Lista de artículos y cantidades
  - Datos del cliente (nombre, email, teléfono)
  - Dirección de entrega completa
  - Notas adicionales (si las hay)

**Ejemplo de email:**
```
============================================================
        RESUMEN DIARIO DE PEDIDOS
        19/11/2025
============================================================

Total de pedidos recibidos: 2
============================================================

PEDIDO #1
Numero de Seguimiento: 123
------------------------------------------------------------

ARTICULOS:
  - Aloe Vera Gel ........................ x2
  - Té Herbal ............................ x1

DATOS DEL CLIENTE:
  Nombre: Juan Pérez
  Email: juan@example.com
  Telefono: +34600000000

DIRECCION DE ENTREGA:
  Calle Example 123
  Sevilla, CP: 41001

============================================================
```

## Ejecución Automática

### Opción 1: Tarea Programada (Windows)

1. Abrir el "Programador de tareas" de Windows
2. Crear una nueva tarea básica
3. Configurar:
   - **Desencadenador:** Diariamente a las 23:59
   - **Acción:** Iniciar programa
   - **Programa:** `python.exe`
   - **Argumentos:** `C:\ruta\al\proyecto\tienda_virtual\run_daily_task.py`
   - **Directorio inicial:** `C:\ruta\al\proyecto\tienda_virtual`

### Opción 2: Tarea Cron (Linux/macOS)

```bash
# Editar crontab
crontab -e

# Añadir línea para ejecutar a las 23:59 diariamente
59 23 * * * cd /ruta/al/proyecto/tienda_virtual && python run_daily_task.py
```

### Opción 3: Render Cron Job

Para el despliegue en Render, se puede crear un Cron Job:

```yaml
# Añadir en render.yaml
- type: cron
  name: daily-order-summary
  env: python
  schedule: "59 23 * * *"
  buildCommand: "pip install -r requirements.txt"
  startCommand: "cd tienda_virtual && python run_daily_task.py"
```

## Personalización

### Cambiar Destinatarios

Editar el archivo `tienda_virtual/home/send_mail.py`:

```python
email = EmailMessage(
    subject=f"Resumen de pedidos del {today.strftime('%d/%m/%Y')}",
    body=body,
    from_email="tu_email@gmail.com",
    to=["admin1@example.com", "admin2@example.com"],  # Lista de destinatarios
)
```

### Modificar Horario de Envío

Ajustar la configuración de la tarea programada o cron job según necesidad.

## Otros Proveedores SMTP

### Outlook/Hotmail
```env
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

### SendGrid
```env
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=tu_api_key_de_sendgrid
```

### Mailgun
```env
EMAIL_HOST=smtp.mailgun.org
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

## Resolución de Problemas

### Error: "SMTPAuthenticationError"
- Verificar que la contraseña de aplicación sea correcta
- Confirmar que la verificación en dos pasos esté activada en Gmail

### Error: "SMTPServerDisconnected"
- Comprobar la conexión a internet
- Verificar que el puerto 587 no esté bloqueado por firewall

### No llegan los emails
1. Revisar la carpeta de spam
2. Verificar que `EMAIL_HOST_USER` sea correcto
3. Comprobar los logs de Django para errores específicos

## Referencias

- [Documentación de Django sobre Email](https://docs.djangoproject.com/en/5.2/topics/email/)
- [Contraseñas de aplicación de Google](https://support.google.com/accounts/answer/185833)
