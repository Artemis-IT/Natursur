# 🚀 TARJETA RÁPIDA - Para Compartir Directamente

## Si Tu Equipo Te Pregunta: "¿Qué Necesito?"

### ✅ RESPUESTA CORTA (30 segundos)
```
Solo Python 3.9+

5 pasos:
  git clone https://github.com/alevelmol/Proyecto-PGPI.git
  cd Proyecto-PGPI
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  cd tienda_virtual
  python manage.py migrate
  python manage.py runserver

Listo. http://127.0.0.1:8000/
```

---

## Si Tu Equipo Te Pregunta: "¿Qué Es?"

### ✅ RESPUESTA MEDIA (2 minutos)
```
Plataforma de nutrición profesional (Natursur)

Funcionalidades:
  ✅ Landing page profesional
  ✅ Registro de usuarios seguro
  ✅ Login flexible (2 opciones)
  ✅ Sistema de citas con calendario
  ✅ Panel administrativo

Tecnología:
  • Django 5.2.6 (Python web framework)
  • SQLite (base de datos)
  • HTML/CSS responsivo

Documentación:
  • README.md - Descripción
  • SETUP.md - Instalación
  • COMANDOS_RAPIDOS.md - Comandos útiles
```

---

## Si Tu Equipo Te Pregunta: "¿Qué Necesito Instalar?"

### ✅ RESPUESTA TÉCNICA (5 minutos)

**Sistema:**
- Python 3.9+ (mínimo: 3.9, recomendado: 3.10+)
- Git (para clonar)

**Dependencias de código:**
- Django 5.2.6 (instalado automáticamente con pip)

**Base de datos:**
- SQLite (incluido con Python)

**No necesitas:**
- PostgreSQL, MySQL, etc
- Node.js
- Docker
- Ningún otro servidor externo

---

## Si Tu Equipo Te Pregunta: "¿Cuánto Tiempo Tarda?"

### ✅ CRONOGRAMA REAL

| Paso | Descripción | Tiempo |
|------|-------------|--------|
| 1 | Instalar Python | ~5 min (o ya está) |
| 2 | git clone | ~1 min |
| 3 | Crear venv | ~1 min |
| 4 | Activar venv | ~10 seg |
| 5 | pip install -r | ~2 min |
| 6 | Migrar BD | ~1 min |
| 7 | runserver | ~10 seg |
| **TOTAL** | **Del cero al funcionando** | **~10 minutos** |

---

## Si Tu Equipo Te Pregunta: "¿Dónde Está la Documentación?"

### ✅ MAPA DE ARCHIVOS

```
COMIENZA AQUÍ:          README.md
CÓMO INSTALAR:          SETUP.md
COMANDOS ÚTILES:        COMANDOS_RAPIDOS.md

REFERENCIAS:
  Estructura completa:   DIAGRAMA_VISUAL.md
  Para producción:       PRODUCCION.md
  Qué hay en el repo:    CHECKLIST_GITHUB.md

PARA COMPARTIR:
  Resumen para líder:    RESUMEN_EQUIPO.md
  Guión de explicación:  GUION_PRESENTACION.md
  Índice de referencias: INDICE_COMPLETO.md
```

---

## Si Tu Equipo Te Pregunta: "¿Es Seguro?"

### ✅ MEDIDAS DE SEGURIDAD

```
✅ Contraseñas hasheadas (PBKDF2 - Django estándar)
✅ Email único validado
✅ Respuestas de seguridad hasheadas
✅ CSRF tokens en formularios
✅ @login_required en rutas protegidas
✅ Input validation en todos los formularios
✅ No hay SQL injection (Django ORM)
✅ Mensajes de error no exponen DB
```

---

## Si Tu Equipo Te Pregunta: "¿Puedo Contribuir?"

### ✅ FLUJO GIT

```bash
# 1. Crear rama desde main
git checkout -b feature/mi-feature

# 2. Hacer cambios
# ... editar código ...

# 3. Commit
git add .
git commit -m "Descripción clara del cambio"

# 4. Push
git push origin feature/mi-feature

# 5. Pull Request en GitHub
# (descripción, revisión, merge)
```

---

## Si Tu Equipo Pregunta: "¿Y si Algo No Funciona?"

### ✅ TROUBLESHOOTING RÁPIDO

```bash
# Error: "No module named 'django'"
→ Verificar que venv está activado
→ Ejecutar: pip install -r requirements.txt

# Error: "Port 8000 already in use"
→ Ejecutar: python manage.py runserver 8080

# Error: "Database error"
→ Ejecutar: python manage.py migrate

# Error: "db.sqlite3 corrupted"
→ Eliminar: rm db.sqlite3
→ Recrear: python manage.py migrate

Más soluciones en: SETUP.md → Troubleshooting
```

---

## Si Tu Equipo Pregunta: "¿Cómo Despliego?"

### ✅ BÁSICO (desarrollo)

```bash
python manage.py runserver 0.0.0.0:8000
# Accesible desde: http://tu-ip:8000/
```

### ✅ PRODUCCIÓN

Ver archivo: **PRODUCCION.md**

Opciones:
- Heroku (más fácil)
- DigitalOcean (más control)
- AWS/GCP (más poder)

Cambios necesarios:
- DEBUG = False
- SECRET_KEY nueva
- ALLOWED_HOSTS = tu dominio
- BD: PostgreSQL (recomendado)
- Gunicorn + Nginx

---

## Si Tu Equipo Pregunta: "¿Cuál es la Estructura?"

### ✅ CARPETAS PRINCIPALES

```
tienda_virtual/
├── tienda_virtual/       (Configuración)
│   ├── settings.py       (DEBUG, INSTALLED_APPS)
│   ├── urls.py           (Rutas principales)
│   └── wsgi.py           (Para producción)
│
└── home/                 (La aplicación principal)
    ├── models.py         (BD: Appointment, SecurityProfile)
    ├── views.py          (Lógica: vistas)
    ├── forms.py          (Formularios)
    ├── urls.py           (Rutas de app)
    ├── admin.py          (Panel admin)
    ├── static/css/       (Estilos)
    └── templates/home/   (HTML)
```

---

## Si Tu Equipo Pregunta: "¿Qué Comandos Uso?"

### ✅ LOS 5 MÁS IMPORTANTES

```bash
# 1. Servidor (desarrollo)
python manage.py runserver

# 2. Migraciones (BD)
python manage.py migrate

# 3. Crear usuario admin
python manage.py createsuperuser

# 4. Shell interactivo
python manage.py shell

# 5. Ver ayuda
python manage.py help
```

Más comandos en: **COMANDOS_RAPIDOS.md**

---

## Si Tu Equipo Pregunta: "¿Cuáles son las URLs?"

### ✅ RUTAS DEL PROYECTO

```
/                          Landing page
/citas/                    Listado de citas (@login_required)
/citas/nueva/              Crear cita (@login_required)
/accounts/register/        Registro
/accounts/login/           Login
/accounts/logout/          Logout
/admin/                    Panel administrativo
```

---

## Si Tu Equipo Pregunta: "¿Necesito Algo Extra?"

### ✅ RESPUESTA: NO

```
❌ NO necesitas: PostgreSQL
❌ NO necesitas: Node.js
❌ NO necesitas: Docker
❌ NO necesitas: Redis
❌ NO necesitas: Nginx configurado
❌ NO necesitas: Certificados SSL (para desarrollo)
❌ NO necesitas: Keys de terceros

✅ TODO lo que necesitas está en el repo
✅ TODO funciona con Python únicamente
✅ TODO está documentado
```

---

## Si Tu Equipo Pregunta: "¿Cuánto Tiempo Mantener?"

### ✅ ESTIMACIÓN

**Semana 1:** Instalación y familiarización
**Semana 2:** Entender arquitectura
**Semana 3:** Primeras contribuciones
**Semana 4+:** Desarrollo normal + mantenimiento

Total: 4 semanas de onboarding normal

---

## TARJETA PARA IMPRIMIR / COMPARTIR

```
╔═══════════════════════════════════════════════════════╗
║         🌿 PROYECTO NATURSUR - QUICK START          ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  REQUISITO: Python 3.9+                             ║
║                                                       ║
║  INSTALACIÓN:                                        ║
║  $ git clone https://github.com/alevelmol/...       ║
║  $ cd Proyecto-PGPI                                  ║
║  $ python -m venv venv                               ║
║  $ .\venv\Scripts\Activate.ps1                       ║
║  $ pip install -r requirements.txt                   ║
║  $ cd tienda_virtual                                 ║
║  $ python manage.py migrate                          ║
║  $ python manage.py runserver                        ║
║                                                       ║
║  ACCESO: http://127.0.0.1:8000/                     ║
║  ADMIN:  http://127.0.0.1:8000/admin/               ║
║                                                       ║
║  DOCUMENTACIÓN: Ver archivos .md en el repo          ║
║                                                       ║
║  TIEMPO: ~5-10 minutos para empezar                 ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

---

## RESUMEN PARA COPIAR-PEGAR

```
Si alguien pregunta "¿qué necesito para el proyecto?"

RESPUESTA CORTA (30 seg):
"Solo Python. Clona el repo, sigue SETUP.md, 5 pasos, 
listo en 5 minutos."

RESPUESTA MEDIA (2 min):
"Es una plataforma de nutrición con registro, login, 
y sistema de citas. Usa Django + SQLite. Documentación 
en el repo. Instalación en README.md y SETUP.md."

RESPUESTA TÉCNICA (5 min):
"Python 3.9+, Django 5.2.6, SQLite. 
git clone → venv → pip install -r → migrate → runserver. 
Toda la documentación está en .md files."
```

---

## ARCHIVOS PARA DIFERENTES PERSONAS

**Si es tu JEFE:**
→ Envía: RESUMEN_EQUIPO.md

**Si es NUEVO en el EQUIPO:**
→ Envía: README.md + SETUP.md

**Si es EXPERIMENTADO:**
→ Envía: COMANDOS_RAPIDOS.md

**Si VAa A DESPLEGAR:**
→ Envía: PRODUCCION.md

**Si PRESENTAS AL EQUIPO:**
→ Lee: GUION_PRESENTACION.md

---

**¡TODO LISTO PARA COMPARTIR!** 🚀
