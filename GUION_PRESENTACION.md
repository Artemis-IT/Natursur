# 📢 Guión de Presentación para el Equipo

## Cuando Compartas el Enlace de GitHub

### Opción 1: Presentación Rápida (2 minutos)

```
"¡Hola equipo! El proyecto está en GitHub.

Para ejecutarlo, necesitan:
- Python 3.9+
- Seguir el archivo SETUP.md

En resumen:
  1. git clone https://github.com/alevelmol/Proyecto-PGPI.git
  2. python -m venv venv
  3. .\venv\Scripts\Activate.ps1
  4. pip install -r requirements.txt
  5. cd tienda_virtual && python manage.py migrate
  6. python manage.py runserver

Listo. En 5 minutos tienen la app corriendo.

Preguntas? Están en:
  - README.md: Qué es
  - SETUP.md: Cómo instalar
  - COMANDOS_RAPIDOS.md: Comandos útiles"
```

---

## Opción 2: Presentación Detallada (5 minutos)

```
"¡Proyecto Natursur en GitHub!

📋 QUÉ ES:
- Plataforma de nutrición con landing page profesional
- Sistema de registro seguro
- Autenticación flexible (email+contraseña O email+pregunta)
- Sistema de citas con calendario
- Panel administrativo

⚡ LO MÁS IMPORTANTE:
Solo necesitas Python. TODO lo demás está.

📦 DEPENDENCIAS:
- Django 5.2.6 (el archivo requirements.txt lo instala)

🚀 INSTALACIÓN (5 PASOS):
1. Clonar: git clone ...
2. Entorno: python -m venv venv
3. Activar: .\venv\Scripts\Activate.ps1
4. Instalar: pip install -r requirements.txt
5. Ejecutar: python manage.py runserver

🛠 ESTRUCTURA:
- /tienda_virtual/           → Proyecto Django
- /tienda_virtual/home/      → App con toda la lógica
- /home/static/css/          → Estilos (Montserrat, verde)
- /home/templates/           → Plantillas HTML

📖 DOCUMENTACIÓN:
- README.md: Descripción completa
- SETUP.md: Instalación paso a paso
- COMANDOS_RAPIDOS.md: Comandos frecuentes
- PRODUCCION.md: Para desplegar

🔐 SEGURIDAD:
- Contraseñas hasheadas
- Email único validado
- Respuestas de seguridad hasheadas
- CSRF tokens
- @login_required en rutas protegidas

✅ VERIFICACIÓN:
Si ves http://127.0.0.1:8000/ con navbar verde y logo Natursur,
¡TODO FUNCIONA!"
```

---

## Opción 3: Por E-mail

```
Asunto: 📦 Proyecto Natursur - GitHub Listo

Hola equipo,

El proyecto está en GitHub y listo para ejecutar:
https://github.com/alevelmol/Proyecto-PGPI

✅ SISTEMA OPERATIVO: Windows / macOS / Linux

✅ REQUISITOS:
- Python 3.9+ (descargar de python.org)

✅ INSTALACIÓN RÁPIDA:
  git clone https://github.com/alevelmol/Proyecto-PGPI.git
  cd Proyecto-PGPI
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  cd tienda_virtual
  python manage.py migrate
  python manage.py runserver

Luego abran: http://127.0.0.1:8000/

✅ DOCUMENTACIÓN:
  - README.md: Qué es el proyecto
  - SETUP.md: Instrucciones paso a paso
  - COMANDOS_RAPIDOS.md: Comandos frecuentes

📞 PREGUNTAS?
  - Ver los archivos .md primero
  - Crear un Issue en GitHub
  - Preguntarme directamente

¡Listo para trabajar juntos!
```

---

## Opción 4: Para Presentación en Video

```
SCRIPT DE VIDEO (3 minutos):

[PANTALLA 1] Mostrar GitHub repo
"Este es el repositorio del proyecto Natursur. 
Todo el código, documentación y guías están aquí."

[PANTALLA 2] Mostrar README.md
"El README explica qué es el proyecto:
- Landing page de nutrición
- Sistema de registro y login
- Sistema de citas
- Panel administrativo"

[PANTALLA 3] Mostrar SETUP.md
"El SETUP.md tiene instrucciones paso a paso.
Pero en resumen, son 8 comandos:"

[MOSTRAR TERMINAL - ESCRIBIR COMANDOS]
1. git clone https://github.com/alevelmol/Proyecto-PGPI.git
2. cd Proyecto-PGPI
3. python -m venv venv
4. .\venv\Scripts\Activate.ps1
5. pip install -r requirements.txt
6. cd tienda_virtual
7. python manage.py migrate
8. python manage.py runserver

[PANTALLA 5] Ejecutando
"En 5 minutos, el proyecto está corriendo..."

[MOSTRAR http://127.0.0.1:8000/]
"Voilà! Landing page con navbar verde, logo Natursur.
Sistema de citas, registro, login... todo funciona."

[PANTALLA 6] Archivos Importantes
"La documentación está en estos archivos:
- requirements.txt: Dependencias (solo Django!)
- README.md: Descripción completa
- SETUP.md: Cómo instalar
- COMANDOS_RAPIDOS.md: Comandos útiles
- PRODUCCION.md: Para desplegar en servidor"

[PANTALLA 7] Resumen
"Necesitasolo Python.
El archivo requirements.txt instala lo demás.
Toda la documentación está en el repo.
¡Listo para trabajar en equipo!"
```

---

## Checklist de Comunicación

### Antes de Compartir
```
✅ Archivos de documentación creados
✅ requirements.txt con versión correcta
✅ .gitignore configurado
✅ README.md claro
✅ SETUP.md con pasos exactos
```

### Al Compartir
```
✅ Enviar enlace de GitHub
✅ Mencionar: "Solo necesitan Python"
✅ Punto al SETUP.md
✅ Decir: "Contactenme si hay problemas"
```

### Después de Compartir
```
✅ Monitorear Issues/PR en GitHub
✅ Responder preguntas rápido
✅ Crear FAQ si hay patrones
✅ Actualizar documentación con feedback
```

---

## Preguntas que Harán (y Respuestas)

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué necesito instalar? | Solo Python. El archivo requirements.txt instala Django. |
| ¿En qué puerto corre? | 8000 por defecto. Cambiar con runserver 8080 |
| ¿Necesito PostgreSQL? | No. SQLite está incluido. |
| ¿Necesito Node.js? | No. Es un proyecto puro Django. |
| ¿Funciona en Mac/Linux? | Sí. Cambiar solo el comando de activar venv. |
| ¿Cómo creo un usuario admin? | python manage.py createsuperuser |
| ¿Cómo reseteo la BD? | rm db.sqlite3 && python manage.py migrate |
| ¿Dónde están los comandos? | En COMANDOS_RAPIDOS.md |
| ¿Cómo despliego? | Ver PRODUCCION.md (Heroku, DigitalOcean, etc) |

---

## 🎯 Puntos Clave para Enfatizar

1. **"Solo necesitan Python"**
   - Es fácil. Una sola dependencia.

2. **"Todo está documentado"**
   - Cada pregunta tiene respuesta en los .md

3. **"Funciona inmediatamente"**
   - Sin configuración. Sin secretos por revelar.

4. **"Es producción-ready"**
   - Seguridad, validación, BD, admin... todo.

5. **"Escalable"**
   - Fácil agregar features. Estructura Django estándar.

---

## 📊 Comparación: Antes vs Después

### ANTES (sin documentación)
```
"¿Cómo executo el proyecto?"
"Eh... instalas Django primero..."
"¿Cómo?"
"Pip install..."
"¿Qué más?"
"Ejecutas migrate..."
"¿Cómo?"
... 30 minutos de preguntas
```

### DESPUÉS (con documentación)
```
"¿Cómo ejecuto el proyecto?"
"Lee el SETUP.md. Sigue los 5 pasos."
5 minutos después...
"¡Funcionó!"
```

---

## 🎁 Bonus: Ejemplo de Interacción

**Equipo:** "¿Cómo empezamos?"

**Tú:** "Miren el archivo SETUP.md. Tienen 5 pasos.
El primero es: `git clone https://github.com/alevelmol/Proyecto-PGPI.git`"

**Equipo:** "Listo. ¿Ahora?"

**Tú:** "Sigan el paso 2 del SETUP.md"

...5 minutos después...

**Equipo:** "¡Funciona! ¿Ahora cómo hacemos login?"

**Tú:** "Ve al README.md, sección 'Flujo de Uso'. Registro → Auto-login → Citas"

**Equipo:** "¡Perfecto!"

---

## 🚀 Lanzamiento

**DÍA 1:**
- Compartir enlace de GitHub
- Decir: "Seguir SETUP.md"
- Preguntas cortas: responder en Slack
- Si hay confusión: hacer reunión de 15 min

**DÍA 2+:**
- El equipo ya está usando
- Preguntas técnicas más profundas
- Empezar a contribuir
- Hacer Pull Requests

---

## Final: Lo que tu Equipo Dirá

```
"Wow, esto es muy claro"
"Solo necesitamos Python"
"SETUP.md es excelente"
"Funcionó al primer intento"
"¡Mucho mejor que lo usual!"
```

✅ **Éxito garantizado.** 🎉
