# 🚀 Guía de Instalación - Proyecto Natursur

**Elaborado por:** Antonio Luis Jiménez de la Fuente (Project Manager) y el Equipo de Proyecto Natursur.  
**Tech Lead (desarrollo web):** Alejandro Vela Molina.

## Requisitos Previos

Tu equipo necesita tener instalado:

- **Python 3.9+** → [Descargar](https://www.python.org/downloads/)
- **Git** → [Descargar](https://git-scm.com/)
- **SQLite3** (incluido con Python)

## Pasos de Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/alevelmol/Proyecto-PGPI.git
cd Proyecto-PGPI
```

### 2️⃣ Crear y activar entorno virtual

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Navegar a la carpeta del proyecto Django

```bash
cd tienda_virtual
```

### 5️⃣ Aplicar migraciones (crear base de datos)

```bash
python manage.py migrate
```

### 6️⃣ Crear usuario administrativo (opcional)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones y crea un usuario con:
- **Nombre de usuario:** admin
- **Email:** admin@natursur.com
- **Contraseña:** (la que quieras)

### 7️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Deberías ver algo como:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 8️⃣ Acceder a la aplicación

- **Sitio principal:** http://127.0.0.1:8000/
- **Panel de admin:** http://127.0.0.1:8000/admin/

---

## 📁 Estructura del Proyecto

```
proyecto/
├── requirements.txt              # Dependencias
├── README.md                     # Información del proyecto
├── tienda_virtual/               # Carpeta principal Django
│   ├── manage.py                # Script de gestión Django
│   ├── db.sqlite3               # Base de datos (se crea automáticamente)
│   ├── tienda_virtual/          # Configuración del proyecto
│   │   ├── settings.py          # Configuración principal
│   │   ├── urls.py              # URLs principales
│   │   └── wsgi.py              # Para despliegue
│   └── home/                    # Aplicación principal
│       ├── models.py            # Modelos (Appointment, SecurityProfile)
│       ├── views.py             # Vistas (lógica)
│       ├── forms.py             # Formularios
│       ├── admin.py             # Configuración admin
│       ├── urls.py              # URLs de la app
│       ├── static/css/          # Estilos CSS
│       └── templates/home/      # Plantillas HTML
```

---

## 🛠️ Comandos Útiles

| Comando | Descripción |
|---------|-------------|
| `python manage.py runserver` | Inicia servidor de desarrollo |
| `python manage.py migrate` | Aplica migraciones de BD |
| `python manage.py makemigrations` | Crea migraciones de cambios en modelos |
| `python manage.py createsuperuser` | Crea usuario admin |
| `python manage.py shell` | Shell interactivo de Django |
| `python manage.py test` | Ejecuta tests (si hay) |

---

## 🔧 Solución de Problemas

### "No module named 'django'"
- Asegúrate de que el entorno virtual esté activado
- Ejecuta: `pip install -r requirements.txt`

### "Permission denied" al activar venv en PowerShell
Ejecuta como admin:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Puerto 8000 ya está en uso
Usa otro puerto:
```bash
python manage.py runserver 8080
```

### Base de datos corrupta
Elimina `db.sqlite3` y ejecuta:
```bash
python manage.py migrate
```

---

## 📋 Funcionalidades del Proyecto

✅ **Landing Page Profesional** - Página de inicio con navbar verde y branding Natursur

✅ **Sistema de Registro** - Registro con:
- Email único validado
- Contraseña con requisitos de seguridad
- 12 preguntas de seguridad personalizables
- Respuestas hasheadas en BD

✅ **Sistema de Login Flexible** - Dos métodos de autenticación:
- Email + Contraseña (estándar)
- Email + Respuesta de Seguridad

✅ **Auto-login** - Los usuarios se logean automáticamente después de registrarse

✅ **Sistema de Citas** - Panel de citas con:
- Selector de fecha y hora
- Almacenamiento en SQLite
- Tabla de listado de citas
- Notas opcionales

✅ **Panel de Admin** - Gestión de:
- Usuarios registrados
- Citas programadas
- Perfiles de seguridad

---

## 👥 Equipo de Desarrollo

Proyecto desarrollado con Django 5.2.6 y SQLite3

---

## 📝 Notas Importantes

1. **Base de datos local**: `db.sqlite3` es solo para desarrollo. En producción usar PostgreSQL/MySQL.
2. **DEBUG = True**: El servidor en `settings.py` tiene DEBUG habilitado. **Cambiar a False en producción**.
3. **SECRET_KEY**: Cambiar en producción a una clave segura.
4. **Migraciones**: Siempre hacer `migrate` después de `git pull` por si hay cambios en modelos.

---

¡Listo! Tu equipo ya puede ejecutar el proyecto sin problemas 🎉
