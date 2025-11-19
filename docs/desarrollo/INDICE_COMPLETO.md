# 📑 ÍNDICE COMPLETO - Referencia para tu Equipo

**Elaborado por:** Antonio Luis Jiménez de la Fuente (Project Manager) y el Equipo de Proyecto Natursur.  
**Tech Lead (desarrollo web):** Alejandro Vela Molina.

## 🎯 ¿Por dónde empiezo?

### Si estás aquí por primera vez:
1. Lee **README.md** (2 minutos)
2. Lee **SETUP.md** (5 minutos)
3. Sigue los 5 pasos
4. ✅ Ya funciona

---

## 📚 Guía Rápida por Tipo de Usuario

### 👤 SOY NUEVO EN EL PROYECTO
```
Archivo a leer: README.md
Luego ejecutar: SETUP.md (paso a paso)
Referencia rápida: COMANDOS_RAPIDOS.md
```

### 👨‍💼 SOY LÍDER DE EQUIPO
```
Archivo a revisar: RESUMEN_EQUIPO.md
Cómo explicar: GUION_PRESENTACION.md
Verificar: CHECKLIST_GITHUB.md
```

### 👨‍💻 SOY DESARROLLADOR
```
Cómo instalar: SETUP.md
Comandos útiles: COMANDOS_RAPIDOS.md
Estructura: README.md → Modelos de BD
Contribuir: Crear rama, hacer cambios, PR
```

### 🚀 VOY A DESPLEGAR A PRODUCCIÓN
```
Leer primero: PRODUCCION.md
Checklist: Punto 5 de PRODUCCION.md
Cambios de código: settings.py (DEBUG, SECRET_KEY)
```

### ❓ TENGO UN PROBLEMA
```
Soluciones comunes: SETUP.md → Troubleshooting
Comandos de debug: COMANDOS_RAPIDOS.md
Estructura: README.md → Modelos de BD
```

---

## 📄 Descripción de Cada Archivo

### 🎯 CORE (Esenciales - Leer Primero)

| Archivo | Propósito | Tiempo | Debe Leer |
|---------|-----------|--------|-----------|
| **README.md** | Descripción del proyecto | 3 min | ✅ TODOS |
| **SETUP.md** | Cómo instalar paso a paso | 5 min | ✅ TODOS |
| **requirements.txt** | Dependencias Python | - | ✅ pip install -r |

### 📋 REFERENCIA (Para Consultar)

| Archivo | Propósito | Tiempo | Leer Cuando |
|---------|-----------|--------|------------|
| **COMANDOS_RAPIDOS.md** | Comandos frecuentes | 2 min | Necesitas ejecutar algo |
| **README.md** | Modelos y rutas | - | Necesitas entender BD |
| **.env.example** | Variables de entorno | 1 min | Vas a producción |

### 🎓 EDUCATIVO (Aprender)

| Archivo | Propósito | Tiempo | Leer Cuando |
|---------|-----------|--------|------------|
| **DIAGRAMA_VISUAL.md** | Visualización completa | 5 min | Quiero entender todo |
| **RESUMEN_EQUIPO.md** | Resumen ejecutivo | 3 min | Necesito presentar |
| **GUION_PRESENTACION.md** | Cómo explicar | - | Voy a explicar al equipo |

### 🚀 PRODUCCIÓN (Para Desplegar)

| Archivo | Propósito | Tiempo | Leer Cuando |
|---------|-----------|--------|------------|
| **PRODUCCION.md** | Despliegue en producción | 10 min | ✅ ANTES de desplegar |
| **CHECKLIST_GITHUB.md** | Qué hay en repo | 5 min | Necesito saber qué subir |

---

## 🗺️ Mapa de Contenidos

```
PROYECTO-PGPI/
│
├─── 🎯 INICIO RÁPIDO
│    ├── README.md                (¿Qué es esto?)
│    ├── SETUP.md                 (¿Cómo lo ejecuto?)
│    └── requirements.txt          (¿Qué instalo?)
│
├─── 📚 REFERENCIAS
│    ├── COMANDOS_RAPIDOS.md      (Comandos útiles)
│    ├── CHECKLIST_GITHUB.md      (Qué hay aquí)
│    └── .env.example             (Variables de entorno)
│
├─── 🎓 DOCUMENTACIÓN AVANZADA
│    ├── DIAGRAMA_VISUAL.md       (Toda la estructura)
│    ├── PRODUCCION.md            (Desplegar en servidor)
│    ├── RESUMEN_EQUIPO.md        (Para presentar)
│    └── GUION_PRESENTACION.md    (Cómo explicar)
│
├─── 🔒 CONFIGURACIÓN
│    ├── .gitignore               (Qué no subir)
│    ├── .env.example             (Variables ejemplo)
│    └── requirements.txt          (Dependencias exactas)
│
└─── 💻 CÓDIGO (tienda_virtual/)
     ├── manage.py                (Control Django)
     ├── tienda_virtual/          (Configuración)
     └── home/                    (La aplicación)
```

---

## 🔍 Búsqueda Rápida

### ¿Necesito...

| Necesidad | Solución | Archivo |
|-----------|----------|---------|
| Instalar el proyecto? | Sigue los pasos 1-5 | SETUP.md |
| Ejecutar el servidor? | `python manage.py runserver` | COMANDOS_RAPIDOS.md |
| Ver lista de citas? | Click en "Citas" luego login | README.md → Flujo |
| Registrarme? | Click en "Iniciar sesión" → Registrarse | README.md → Registro |
| Crear usuario admin? | `python manage.py createsuperuser` | COMANDOS_RAPIDOS.md |
| Entrar a admin? | http://127.0.0.1:8000/admin/ | README.md → URLs |
| Cambiar contraseña de admin? | `python manage.py changepassword admin` | COMANDOS_RAPIDOS.md |
| Ver estructura del proyecto? | Copia la carpeta home/ | README.md → Estructura |
| Desplegar a producción? | Lee primero PRODUCCION.md | PRODUCCION.md |
| Arreglar puerto en uso? | `python manage.py runserver 8080` | SETUP.md → Troubleshooting |
| Resetear base de datos? | `rm db.sqlite3 && migrate` | COMANDOS_RAPIDOS.md |
| Ver lista de migraciones? | `python manage.py showmigrations` | COMANDOS_RAPIDOS.md |
| Agregar una nueva feature? | Crear rama en Git | README.md → Contribuir |
| Cambiar configuración? | Editar settings.py | README.md → settings |
| Entender modelos de BD? | Ver apartado Modelos de BD | README.md |

---

## 👥 Roles en el Equipo

### 👨‍💻 DESARROLLADOR
**Archivos importantes:**
1. SETUP.md (instalación)
2. COMANDOS_RAPIDOS.md (comandos)
3. README.md (estructura, modelos)
4. Código en tienda_virtual/

**Flujo típico:**
```
Lunes: git clone + SETUP.md
Miércoles: Entender modelos en README.md
Viernes: Hacer PR con feature nueva
```

### 📊 PROJECT MANAGER / LÍDER
**Archivos importantes:**
1. README.md (descripción general)
2. RESUMEN_EQUIPO.md (para presentar)
3. CHECKLIST_GITHUB.md (que sepa qué hay)
4. GUION_PRESENTACION.md (cómo explicar)

**Flujo típico:**
```
Hoy: Leer RESUMEN_EQUIPO.md
Mañana: Usar GUION_PRESENTACION.md para explicar
Semana: Monitorear PRs en GitHub
```

### 🛠️ OPS / DEVOPS
**Archivos importantes:**
1. PRODUCCION.md (despliegue)
2. README.md (settings.py)
3. COMANDOS_RAPIDOS.md (comandos DB)
4. .env.example (variables)

**Flujo típico:**
```
Análisis: Leer PRODUCCION.md
Preparación: Cambiar settings.py
Deploy: Seguir checklist PRODUCCION.md
Monitoreo: Logs y backup
```

### 🧪 QA / TESTER
**Archivos importantes:**
1. README.md (funcionalidades)
2. SETUP.md (instalar)
3. COMANDOS_RAPIDOS.md (reset de BD)
4. GUION_PRESENTACION.md (flujos)

**Flujo típico:**
```
Setup: Instalar 3 veces (probar SETUP.md)
Testing: Registro → Login → Citas
Reset: rm db.sqlite3 + migrate para tests limpios
Report: Issues en GitHub
```

---

## ⏱️ Cronograma Sugerido

### DÍA 1 (TÚ)
```
09:00 → Compartir GitHub link
09:30 → Enviar SETUP.md al equipo
10:00 → Disponible para preguntas
```

### DÍA 1 (EQUIPO - 10 minutos de cada uno)
```
10:00 → Clonar repo
10:05 → Seguir SETUP.md
10:15 → `python manage.py runserver`
10:20 → ✅ "Funciona!"
```

### DÍA 2
```
09:00 → Todos en mismo servidor
09:30 → Familiarización con UI
10:00 → Primeras contribuciones
```

### DÍA 3+
```
Desarrollo normal
PRs y reviews
Nuevas features
```

---

## 📞 Preguntas Frecuentes Ubicadas

| Pregunta | Respuesta en |
|----------|--------------|
| ¿Qué necesito instalar? | SETUP.md → Requisitos |
| ¿Cómo instalo? | SETUP.md → Pasos |
| ¿Qué es el proyecto? | README.md → Descripción |
| ¿Qué dependencias hay? | requirements.txt (solo 1) |
| ¿Cómo creo citas? | README.md → Flujo de Uso |
| ¿Cómo registro usuario? | README.md → Flujo de Uso |
| ¿Cómo despliego? | PRODUCCION.md |
| ¿Dónde está el admin? | http://127.0.0.1:8000/admin/ |
| ¿Qué comandos uso? | COMANDOS_RAPIDOS.md |
| ¿Qué puedo contribuir? | README.md → Contribuir |
| ¿Hay errores? | SETUP.md → Troubleshooting |
| ¿Necesito PostgreSQL? | No, SQLite está incluido |
| ¿En qué puerto corre? | 8000 (cambiar con runserver 8080) |

---

## ✅ Checklist de Lectura para Equipo Nuevo

### Primeros 15 minutos
- [ ] Lea README.md (entienda qué es)
- [ ] Lea SETUP.md (primeros pasos)
- [ ] Note que necesita Python 3.9+

### Siguientes 5 minutos
- [ ] Ejecute: `git clone ...`
- [ ] Ejecute: `python -m venv venv`
- [ ] Ejecute: `.\venv\Scripts\Activate.ps1`

### Siguientes 5 minutos
- [ ] Ejecute: `pip install -r requirements.txt`
- [ ] Ejecute: `cd tienda_virtual`
- [ ] Ejecute: `python manage.py migrate`

### Siguientes 5 minutos
- [ ] Ejecute: `python manage.py runserver`
- [ ] Abra: http://127.0.0.1:8000/
- [ ] ✅ Vea landing page Natursur

### Siguientes 5 minutos
- [ ] Pruebe: Registrarse
- [ ] Pruebe: Crear cita
- [ ] Pruebe: Logout y login
- [ ] ✅ Funciona todo

---

## 🎁 Bonus: Atajos por Rol

**NUEVOS (5 min):**
```
1. Leer: README.md
2. Seguir: SETUP.md
3. Ver: http://127.0.0.1:8000/
```

**EXPERIMENTADOS (10 min):**
```
1. git clone
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver
```

**PRODUCTORES (15 min):**
```
1. Leer: PRODUCCION.md
2. Cambiar: settings.py
3. Deploy: instrucciones en PRODUCCION.md
```

---

## 🎓 Plan de Aprendizaje Sugerido

### SEMANA 1: Instalación y Familiarización
- [ ] SETUP.md completado
- [ ] Proyecto funcionando
- [ ] README.md entendido
- [ ] Primeros tests en UI

### SEMANA 2: Arquitectura
- [ ] Entender modelos (README.md)
- [ ] Entender vistas (código + README.md)
- [ ] Entender templates (código)
- [ ] Entender forms (código)

### SEMANA 3: Desarrollo
- [ ] Crear nueva feature
- [ ] Hacer tests
- [ ] Pull request
- [ ] Code review

### SEMANA 4+: Mantenimiento
- [ ] Revisar PRs
- [ ] Desplegar cambios
- [ ] Monitorear producción
- [ ] Agregar documentación

---

**¡Ahora tu equipo tiene TODO lo que necesita!** 🚀

Cualquier duda, consultar el archivo `.md` apropiado.
