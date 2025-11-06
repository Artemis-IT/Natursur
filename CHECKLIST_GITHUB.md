# 📦 CHECKLIST - Para subir a GitHub

## ✅ Archivos que DEBEN estar en el repositorio

```
✅ requirements.txt           - Dependencias Python (ESENCIAL)
✅ README.md                  - Documentación principal
✅ SETUP.md                   - Guía de instalación paso a paso
✅ PRODUCCION.md              - Configuración para despliegue
✅ .env.example               - Variables de entorno (sin valores secretos)
✅ .gitignore                 - Archivos a ignorar

✅ tienda_virtual/            - Carpeta proyecto Django
   ✅ manage.py
   ✅ tienda_virtual/         - Configuración
      ✅ settings.py
      ✅ urls.py
      ✅ wsgi.py
      ✅ asgi.py
   ✅ home/                   - Aplicación
      ✅ models.py
      ✅ views.py
      ✅ forms.py
      ✅ urls.py
      ✅ admin.py
      ✅ static/css/styles.css
      ✅ templates/home/*.html
      ✅ migrations/
```

## ❌ Archivos que NO deben subirse (están en .gitignore)

```
❌ db.sqlite3                 - Base de datos local
❌ venv/                      - Entorno virtual
❌ __pycache__/               - Archivos compilados
❌ .env                       - Variables secretas (NUNCA subir)
❌ *.log                      - Archivos de logs
❌ .vscode/, .idea/           - Configuración IDE
```

---

## 👥 Lo que tu equipo necesita para ejecutar el proyecto

### 1. Requisitos Mínimos
- **Python 3.9+** instalado
- **Git** para clonar el repositorio
- **pip** (viene con Python)
- Acceso a terminal/PowerShell

### 2. Pasos para tu equipo

```bash
# 1. Clonar el repositorio
git clone https://github.com/alevelmol/Proyecto-PGPI.git
cd Proyecto-PGPI

# 2. Crear entorno virtual (IMPORTANTE)
python -m venv venv

# 3. Activar (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 4. Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# 5. Navegar a la carpeta Django
cd tienda_virtual

# 6. Crear base de datos
python manage.py migrate

# 7. Ejecutar servidor
python manage.py runserver

# ✅ LISTO: http://127.0.0.1:8000/
```

---

## 📋 Resumen de Dependencias

**Total de dependencias:** 1 (Django 5.2.6)

```
Django==5.2.6
```

✅ **Ventaja:** Proyecto muy ligero y sin complejidades externas

Incluido en Django:
- Sistema de autenticación
- ORM para BD
- Admin panel
- Sistema de templates
- Manejo de formularios
- Migraciones automáticas

---

## 🔐 Documentos importantes

| Archivo | Propósito |
|---------|-----------|
| **README.md** | Descripción del proyecto, estructura, características |
| **SETUP.md** | Instrucciones paso a paso para configurar entorno |
| **requirements.txt** | Dependencias Python (esencial para `pip install`) |
| **PRODUCCION.md** | Cambios necesarios antes de subir a producción |
| **.env.example** | Referencia de variables de entorno (sin secretos) |
| **.gitignore** | Archivos a NO subir a GitHub |

---

## 🚀 Checklist Final Antes de Hacer Push

```bash
# Dentro de la carpeta del proyecto

# 1. Verificar archivos
ls -la requirements.txt README.md SETUP.md PRODUCCION.md .env.example

# 2. Verificar que NO hay db.sqlite3 ni venv/ en staging
git status  # No debe aparecer db.sqlite3

# 3. Hacer commit
git add .
git commit -m "Agrega documentación y configuración para GitHub"

# 4. Push
git push origin main
```

---

## 📝 Contenido de cada archivo

### requirements.txt
```
Django==5.2.6
```
**¿Por qué?** Para que `pip install -r requirements.txt` instale exactamente lo necesario.

### SETUP.md
- Instrucciones de instalación paso a paso (Windows/Mac/Linux)
- Cómo activar venv
- Cómo ejecutar migraciones
- Solución de problemas comunes
- Comandos útiles

### README.md
- Descripción del proyecto
- Características principales
- Estructura de carpetas
- Cómo empezar rápido
- Modelos de BD
- Flujo de uso

### PRODUCCION.md
- Cambios de settings.py para seguridad
- Cómo configurar PostgreSQL
- Opciones de despliegue (Heroku, DigitalOcean, etc)
- Checklist pre-producción

### .env.example
- Muestra qué variables de entorno existen
- NO incluye valores secretos
- El equipo copia a .env y llena valores

---

## 🛠️ Para que el equipo NO tenga problemas

✅ **Documentación clara:** Toda la info está en README + SETUP.md

✅ **requirements.txt:** Una línea, fácil de instalar

✅ **Entorno aislado:** Con venv no hay conflictos de versiones

✅ **Base de datos automática:** `manage.py migrate` la crea

✅ **Sin secretos:** .gitignore excluye db.sqlite3 y .env

✅ **Comandos listos:** Todos los comandos están documentados

---

## 📞 Resumen para tu Equipo

Tu equipo debe:

1. **Clonar el repo:** `git clone ...`
2. **Instalar dependencias:** `pip install -r requirements.txt`
3. **Crear BD:** `python manage.py migrate`
4. **Ejecutar:** `python manage.py runserver`

**Eso es todo.** Nada más complicado.

---

## ⚠️ Notas Importantes

- El proyecto NO necesita bases de datos externas (SQLite funciona)
- El proyecto NO necesita librerías externas complejas
- El proyecto está listo para producción con cambios mínimos (ver PRODUCCION.md)
- Todos los mensajes de error están en español
- El diseño es responsivo y profesional

---

**¿Listo para GitHub?** 🚀
