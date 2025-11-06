# 🌿 Natursur - Sistema de Gestión de Nutrición

**Proyecto PGPI** - Plataforma web profesional para gestión de citas y servicios de nutrición.

**Elaborado por:** Antonio Luis Jiménez de la Fuente (Project Manager) y el Equipo de Proyecto Natursur. 
**Tech Lead (desarrollo web):** Alejandro Vela Molina.

![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![Django](https://img.shields.io/badge/Django-5.2.6-darkgreen)
![SQLite](https://img.shields.io/badge/BD-SQLite3-blue)

---

## 🎯 Descripción del Proyecto

**Natursur** es una plataforma web moderna de nutrición que permite:

- 🏠 **Landing page profesional** con navbar verde y branding corporativo
- 👤 **Registro seguro** con validación de email y preguntas de seguridad
- 🔐 **Autenticación flexible** - Email+Contraseña o Email+Pregunta de Seguridad
- 📅 **Sistema de citas** con selector de fecha/hora y almacenamiento en BD
- 🛠️ **Panel administrativo** para gestionar citas y usuarios
- 📱 **Diseño responsivo** con fuente Montserrat y colores corporativos

---

## ⚡ Inicio Rápido

```bash
# 1. Clonar repositorio
git clone https://github.com/alevelmol/Proyecto-PGPI.git
cd Proyecto-PGPI

# 2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# source venv/bin/activate  # macOS/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Navegar a proyecto Django
cd tienda_virtual

# 5. Migrar base de datos
python manage.py migrate

# 6. Ejecutar servidor
python manage.py runserver
```

**Acceder a:** http://127.0.0.1:8000/

📖 **Instrucciones detalladas:** Ver [SETUP.md](./SETUP.md)

---

## 📋 Requisitos del Sistema

| Requisito | Versión |
|-----------|---------|
| Python | 3.9 o superior |
| Django | 5.2.6 |
| SQLite | 3.0+ (incluido con Python) |
| Sistema Operativo | Windows, macOS, Linux |

---

## 🎨 Características Principales

### 1. **Landing Page Profesional**
- Navbar verde fijo (#2a9d8f)
- Secciones de Beneficios, Productos, Citas y Contacto
- Branding "Powered by Artemis IT"
- Diseño responsivo y atractivo

### 2. **Sistema de Registro Seguro**
```
✓ Email único validado
✓ Contraseña con requisitos (8+ caracteres, diversidad)
✓ 12 preguntas de seguridad personalizables
✓ Respuestas hasheadas en base de datos
✓ Mensajes de error en español
```

### 3. **Autenticación Flexible**
```
Opción 1: Email + Contraseña (método estándar Django)
Opción 2: Email + Respuesta de Seguridad (método personalizado)
```

### 4. **Sistema de Citas**
- Crear nuevas citas con fecha y hora
- Selector datetime-local en el navegador
- Notas opcionales
- Tabla de listado de citas registradas
- Almacenamiento persistente en SQLite

### 5. **Panel Administrativo**
- Gestión de usuarios registrados
- Listado de todas las citas
- Búsqueda por nombre y email
- Filtros por fecha

---

## 📁 Estructura del Proyecto

```
Proyecto-PGPI/
├── requirements.txt              # Dependencias Python
├── README.md                     # Este archivo
├── SETUP.md                      # Guía de instalación detallada
├── .gitignore                    # Archivos a ignorar en Git
│
└── tienda_virtual/               # 📁 Proyecto Django principal
    ├── manage.py                 # Script de gestión Django
    ├── db.sqlite3                # Base de datos (se crea al migrar)
    │
    ├── tienda_virtual/           # ⚙️ Configuración del proyecto
    │   ├── __init__.py
    │   ├── settings.py           # Configuración (DEBUG, INSTALLED_APPS, etc)
    │   ├── urls.py               # URLs principales del proyecto
    │   ├── asgi.py               # Para despliegue ASGI
    │   └── wsgi.py               # Para despliegue WSGI
    │
    └── home/                     # 🏠 Aplicación principal
        ├── models.py             # Modelos de BD (Appointment, SecurityProfile)
        ├── views.py              # Vistas (lógica de negocio)
        ├── forms.py              # Formularios (Registro, Login, Citas)
        ├── admin.py              # Configuración del panel admin
        ├── urls.py               # URLs de la aplicación
        ├── apps.py               # Configuración de la app
        ├── tests.py              # Tests unitarios
        │
        ├── static/home/          # 📦 Archivos estáticos
        │   └── css/
        │       └── styles.css    # Estilos CSS (verde, Montserrat)
        │
        ├── templates/home/       # 🎨 Plantillas HTML
        │   ├── index.html        # Landing page
        │   ├── register.html     # Formulario de registro
        │   ├── login.html        # Formulario flexible de login
        │   ├── appointments.html # Listado de citas
        │   └── appointment_form.html  # Crear nueva cita
        │
        ├── migrations/           # 🔄 Migraciones de BD
        │   ├── 0001_initial.py   # Crea tabla Appointment
        │   └── 0002_securityprofile.py  # Crea tabla SecurityProfile
        │
        └── __pycache__/          # Archivos compilados Python
```

---

## 🗄️ Modelos de Base de Datos

### `Appointment` - Citas Programadas
```python
- id (auto)
- name: CharField(100)         # Nombre del paciente
- email: EmailField()          # Email del paciente
- datetime: DateTimeField()    # Fecha y hora de cita
- notes: TextField(blank=True) # Notas opcionales
- created_at: DateTimeField()  # Fecha de creación
```

### `SecurityProfile` - Perfil de Seguridad
```python
- user: OneToOneField(User)    # Relación 1:1 con Usuario
- question: CharField(255)     # Pregunta de seguridad seleccionada
- answer: CharField(255)       # Respuesta hasheada con make_password()
```

### `User` (Estándar Django)
```python
- id (auto)
- username: CharField()        # = email
- email: EmailField()          # Email único
- password: CharField()        # Hash de contraseña
- first_name: CharField()      # Nombre
- last_name: CharField()       # Apellidos
- is_active: Boolean()         # Usuario activo
- date_joined: DateTimeField() # Fecha de registro
```

---

## 🚀 Flujo de Uso

### 1. **Visitante → Landing Page**
```
http://127.0.0.1:8000/ → Navbar + Hero + Beneficios + Productos
                        → Contacto + Footer "Powered by Artemis IT"
```

### 2. **Registro de Usuario**
```
Clic en "Iniciar sesión" → Link "Registrarse" 
→ Completa: Nombre, Apellidos, Email, Contraseña (2x), Pregunta seguridad
→ Sistema valida email único + contraseña fuerte
→ Se crea SecurityProfile con respuesta hasheada
→ AUTO-LOGIN: Se logea automáticamente
→ Redirecciona a: Panel de Citas
```

### 3. **Primera Sesión en Panel de Citas**
```
http://127.0.0.1:8000/citas/ 
→ Navbar dinámica con "Hola {nombre}, [Cerrar sesión]"
→ Tabla vacía: "No tienes citas registradas"
→ Botón "Nueva cita" → Formulario datetime + notas
```

### 4. **Crear Cita**
```
/citas/nueva/ → Formulario:
  - Nombre
  - Email
  - Fecha/Hora (selector calendario)
  - Notas (opcional)
→ Guarda en BD SQLite
→ Redirecciona a /citas/ con la cita en tabla
```

### 5. **Logout**
```
Clic "Cerrar sesión" → Limpia sesión → Redirecciona a index
→ Navbar vuelve a mostrar "Iniciar sesión"
```

### 6. **Login Flexible**
```
Opción A: Email + Contraseña
  → Django auth estándar
  
Opción B: Email + Respuesta de Seguridad
  → Valida contra SecurityProfile.check_answer()
  → Usa check_password() para verificar hash
```

---

## 🛠️ Comandos Principales

```bash
# Desarrollo
python manage.py runserver              # Inicia servidor en 127.0.0.1:8000
python manage.py runserver 0.0.0.0:8080 # Puerto personalizado

# Base de Datos
python manage.py migrate                # Aplica todas las migraciones
python manage.py makemigrations         # Crea nuevas migraciones
python manage.py migrate home 0001      # Revierte a migración específica
python manage.py migrate home zero      # Revierte todas las migraciones

# Usuario
python manage.py createsuperuser        # Crea usuario admin
python manage.py changepassword         # Cambia contraseña

# Utilidades
python manage.py shell                  # Shell interactivo Django
python manage.py dbshell                # Shell SQLite
python manage.py collectstatic          # Recopila archivos estáticos
python manage.py test                   # Ejecuta tests
```

---

## 🔐 Seguridad

✅ **Contraseñas:**
- Hasheadas con PBKDF2 (Django default)
- Validadas con requisitos mínimos
- Confirmación en registro

✅ **Respuestas de Seguridad:**
- Hasheadas con make_password()
- Verificadas con check_password()
- No visible en admin (ni al usuario que la ingresa)

✅ **Email:**
- Único a nivel de BD
- Validación de formato
- Usado como username

✅ **Sesiones:**
- CSRF tokens en formularios
- Cookies de sesión seguras
- @login_required en vistas protegidas

---

## 📝 Variables de Entorno

No se requiere `.env` para desarrollo. Para producción crear:

```env
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-segura-aqui
ALLOWED_HOSTS=127.0.0.1,localhost,tudominio.com
DATABASE_URL=postgresql://user:pass@localhost:5432/natursur
```

---

## 🐛 Solución de Problemas

### "ModuleNotFoundError: No module named 'django'"
```bash
# Verificar venv activado
pip install -r requirements.txt
```

### Puerto 8000 en uso
```bash
python manage.py runserver 8080
```

### Base de datos corrupta
```bash
# Eliminar db.sqlite3 y recrear
rm db.sqlite3
python manage.py migrate
```

### Errores de migración
```bash
# Mostrar estado migraciones
python manage.py showmigrations

# Resetear (⚠️ borra datos)
python manage.py migrate home zero
python manage.py migrate
```

📖 **Ver SETUP.md** para más soluciones

---

## 🤝 Contribuir al Proyecto

1. Fork el repositorio
2. Crea rama: `git checkout -b feature/mi-feature`
3. Commit cambios: `git commit -m "Agrega mi-feature"`
4. Push: `git push origin feature/mi-feature`
5. Abre Pull Request

---

## 📄 Licencia

Proyecto educativo PGPI 2024

---

## 👨‍💼 Autor

**Alejandro** - Proyecto PGPI Grupo

- GitHub: [@alevelmol](https://github.com/alevelmol)
- Repositorio: [Proyecto-PGPI](https://github.com/alevelmol/Proyecto-PGPI)

---

## 📞 Soporte

Para problemas o preguntas:
1. Revisar [SETUP.md](./SETUP.md)
2. Consultar Issues en GitHub
3. Contactar al equipo de desarrollo

---

**¡Gracias por usar Natursur!** 🌿