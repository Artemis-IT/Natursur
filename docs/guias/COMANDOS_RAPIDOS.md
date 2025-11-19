# ⚡ Comandos Rápidos - Django Natursur

**Elaborado por:** Antonio Luis Jiménez de la Fuente (Project Manager) y el Equipo de Proyecto Natursur.  
**Tech Lead (desarrollo web):** Alejandro Vela Molina.

## 🚀 Primeros Pasos (Tu Equipo)

```bash
# Clonar
git clone https://github.com/alevelmol/Proyecto-PGPI.git
cd Proyecto-PGPI

# Entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1           # Windows PowerShell
# source venv/bin/activate            # macOS/Linux

# Instalar & Ejecutar
pip install -r requirements.txt
cd tienda_virtual
python manage.py migrate
python manage.py runserver
```

**Listo:** http://127.0.0.1:8000/

---

## 🔧 Comandos de Desarrollo

```bash
# Entorno virtual (dentro de tienda_virtual)
cd tienda_virtual

# Servidor
python manage.py runserver              # Puerto 8000
python manage.py runserver 8080         # Puerto personalizado
python manage.py runserver 0.0.0.0:8000 # Acceso remoto

# Base de datos
python manage.py migrate                # Aplicar migraciones
python manage.py makemigrations home    # Crear migraciones
python manage.py makemigrations         # Todas las apps
python manage.py showmigrations         # Ver estado
python manage.py migrate home 0001      # Revertir a 0001
python manage.py migrate home zero      # Revertir todas

# Usuario admin
python manage.py createsuperuser        # Crear admin
python manage.py changepassword admin   # Cambiar contraseña

# Utilidades
python manage.py shell                  # Shell interactivo
python manage.py dbshell                # Shell SQLite
python manage.py collectstatic          # Recopilar estáticos
python manage.py test                   # Tests

# Limpiar
python manage.py flush                  # Borrar todos datos
```

---

## 👤 Flujo de Registro y Login

### Registrarse
```
1. Clic "Iniciar sesión" en navbar
2. Link "Registrarse" 
3. Llenar formulario:
   - Nombre
   - Apellidos
   - Email (único)
   - Contraseña (8+ caracteres, requisitos)
   - Confirmar contraseña
   - Seleccionar pregunta de seguridad
   - Ingresar respuesta
4. Submit
5. ✅ Auto-logea y redirige a /citas/
```

### Login Opción 1: Email + Contraseña
```
1. Clic "Iniciar sesión"
2. Seleccionar radio "Correo y contraseña"
3. Ingresar email + contraseña
4. Submit
```

### Login Opción 2: Email + Pregunta de Seguridad
```
1. Clic "Iniciar sesión"
2. Seleccionar radio "Pregunta de seguridad"
3. Ingresar email + respuesta
4. Submit
```

---

## 📅 Flujo de Citas

```
1. Clic "Citas" en navbar (redirige a login si no autentico)
2. Ver tabla de citas (vacía si es nuevo usuario)
3. Clic "Nueva cita"
4. Llenar:
   - Nombre
   - Email
   - Fecha/Hora (calendario interactivo)
   - Notas (opcional)
5. Clic "Guardar"
6. ✅ Vuelve a tabla con nueva cita
```

---

## 🛠️ Admin (http://127.0.0.1:8000/admin/)

```bash
# Crear usuario admin
python manage.py createsuperuser

# En admin puedes:
- Ver todos los usuarios registrados
- Ver todas las citas
- Ver perfiles de seguridad
- Editar datos de citas
- Buscar por nombre/email
```

---

## 🐛 Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| "No module named 'django'" | `pip install -r requirements.txt` |
| Puerto 8000 en uso | `python manage.py runserver 8080` |
| "django.db.utils.OperationalError" | `python manage.py migrate` |
| Olvidé contraseña de admin | `python manage.py changepassword admin` |
| DB corrupta | `rm db.sqlite3` + `python manage.py migrate` |
| Cambios CSS no aparecen | `python manage.py collectstatic` |
| Venv no activa en PowerShell | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |

---

## 📁 Estructura Rápida

```
tienda_virtual/
├── manage.py                 # Script principal
├── db.sqlite3               # Base de datos (se crea con migrate)
├── tienda_virtual/          # Configuración
│   ├── settings.py          # DEBUG, INSTALLED_APPS, etc
│   └── urls.py              # Rutas principales
└── home/                    # App principal
    ├── models.py            # BD: Appointment, SecurityProfile
    ├── views.py             # Lógica: index, register, login, citas
    ├── forms.py             # Formularios
    ├── urls.py              # Rutas: citas/, register, login
    ├── static/css/          # CSS (styles.css)
    └── templates/home/      # HTML (5 plantillas)
```

---

## 📊 Modelos de BD Rápido

```python
# Appointment (Citas)
- name: string
- email: email
- datetime: fecha+hora
- notes: texto (opcional)
- created_at: timestamp

# SecurityProfile (Seguridad)
- user: ForeignKey to User
- question: string (la pregunta)
- answer: string (respuesta hasheada)

# User (estándar Django)
- username: email
- email: único
- password: hasheada
- first_name: nombre
- last_name: apellidos
```

---

## 🔐 Seguridad Rápida

✅ Contraseñas: PBKDF2 (Django default)
✅ Respuestas: make_password() + check_password()
✅ Email: Único a nivel de BD
✅ Sesiones: CSRF tokens + cookies
✅ Autenticación: @login_required en vistas

---

## 📱 URLs Principales

```
/                           # Landing page
/accounts/register/         # Registro
/accounts/login/            # Login
/accounts/logout/           # Logout
/citas/                     # Listado de citas (@login_required)
/citas/nueva/              # Crear cita (@login_required)
/admin/                    # Panel admin
```

---

## 🎨 Estilos Principales

```css
Color principal (verde): #2a9d8f
Color secundario: #237a6a
Fuente: Montserrat Medium (font-weight: 500)
Responsive: Sí (media queries para mobile)
```

---

## 📦 Deploy (Producción)

```bash
# 1. Cambiar settings.py
# DEBUG = False
# SECRET_KEY = nueva clave segura
# ALLOWED_HOSTS = tu dominio

# 2. Instalar Gunicorn
pip install gunicorn

# 3. Ejecutar con Gunicorn
gunicorn tienda_virtual.wsgi --bind 0.0.0.0:8000

# 4. Usar Nginx como proxy reverso

# Ver PRODUCCION.md para detalles
```

---

## 🎓 Apuntes para el Equipo

- **Django ORM:** No escribimos SQL, Django lo genera
- **Migraciones:** Versión control de la BD
- **@login_required:** Protege vistas sin autenticación
- **make_password():** Hashea contraseñas de forma segura
- **Django Admin:** Auto-generado para gestionar datos
- **Templates:** HTML con variables Python {{ var }}
- **Forms:** Validación automática de datos
- **Sesiones:** Django maneja cookies automáticamente

---

**¡Comandos listos para usar!** 🚀
