# Documentación del Proyecto Natursur

Bienvenido a la documentación completa del proyecto **Natursur** - Tienda Virtual.

---

## 🆕 ¡Nuevas Funcionalidades!

**¿Buscas información sobre las últimas funcionalidades implementadas?**

👉 **[Ver Nuevas Funcionalidades](./NUEVAS_FUNCIONALIDADES.md)** - Resumen ejecutivo de:
- Sistema de notificaciones SMS (Twilio)
- Resumen diario de pedidos por email
- Despliegue en Render (Cloud)
- Gestión de variables de entorno

---

## 📂 Estructura de la Documentación

La documentación está organizada en las siguientes categorías:

### 🔧 [Setup y Configuración](./setup/)

Guías para configurar el entorno de desarrollo y producción:

- **[SETUP.md](./setup/SETUP.md)** - Configuración inicial del proyecto
- **[VARIABLES_ENTORNO.md](./setup/VARIABLES_ENTORNO.md)** - Guía completa de variables de entorno
- **[SCRAPING_SETUP.md](./setup/SCRAPING_SETUP.md)** - Configuración del web scraping
- **[PRODUCCION.md](./setup/PRODUCCION.md)** - Despliegue en producción
- **[RENDER_DESPLIEGUE.md](./setup/RENDER_DESPLIEGUE.md)** - Despliegue en Render (Cloud)
- **[TWILIO_CONFIGURACION.md](./setup/TWILIO_CONFIGURACION.md)** - Configuración de envío de SMS
- **[EMAIL_CONFIGURACION.md](./setup/EMAIL_CONFIGURACION.md)** - Configuración de envío de emails
- **[install_dependencies.ps1](./setup/install_dependencies.ps1)** - Script de instalación automática
- **[run_scraping.ps1](./setup/run_scraping.ps1)** - Script para ejecutar web scraping

### 📚 [Guías de Uso](./guias/)

Guías rápidas para usuarios y desarrolladores:

- **[COMANDOS_RAPIDOS.md](./guias/COMANDOS_RAPIDOS.md)** - Comandos útiles del proyecto
- **[PRODUCTOS_INICIO_RAPIDO.md](./guias/PRODUCTOS_INICIO_RAPIDO.md)** - Cómo añadir productos rápidamente
- **[TARJETA_RAPIDA.md](./guias/TARJETA_RAPIDA.md)** - Referencia rápida del proyecto
- **[TESTS_RUN.md](./guias/TESTS_RUN.md)** - Cómo ejecutar tests

### 💻 [Desarrollo](./desarrollo/)

Documentación técnica y de desarrollo:

- **[CHANGELOG.md](./desarrollo/CHANGELOG.md)** - Historial de cambios y nuevas funcionalidades
- **[SCRAPING_PRODUCTOS.md](./desarrollo/SCRAPING_PRODUCTOS.md)** - Detalles del sistema de scraping
- **[DIAGRAMA_VISUAL.md](./desarrollo/DIAGRAMA_VISUAL.md)** - Diagramas de arquitectura
- **[FAVICON.md](./desarrollo/FAVICON.md)** - Gestión de favicons
- **[INDICE_COMPLETO.md](./desarrollo/INDICE_COMPLETO.md)** - Índice completo del código
- **[CHECKLIST_GITHUB.md](./desarrollo/CHECKLIST_GITHUB.md)** - Checklist para GitHub

### 👥 [Equipo](./equipo/)

Información del equipo y presentaciones:

- **[RESUMEN_EQUIPO.md](./equipo/RESUMEN_EQUIPO.md)** - Resumen del equipo de desarrollo
- **[GUION_PRESENTACION.md](./equipo/GUION_PRESENTACION.md)** - Guión para presentaciones
- **[RESPUESTA_FINAL.md](./equipo/RESPUESTA_FINAL.md)** - Documento de respuesta final

---

## 🚀 Inicio Rápido

Si es la primera vez que trabajas con el proyecto:

1. **Configuración Inicial:** Lee [SETUP.md](./setup/SETUP.md)
2. **Variables de Entorno:** Configura según [VARIABLES_ENTORNO.md](./setup/VARIABLES_ENTORNO.md)
3. **Instalación Rápida:** Ejecuta [install_dependencies.ps1](./setup/install_dependencies.ps1)
4. **Comandos Básicos:** Consulta [COMANDOS_RAPIDOS.md](./guias/COMANDOS_RAPIDOS.md)
5. **Referencia Rápida:** Revisa [TARJETA_RAPIDA.md](./guias/TARJETA_RAPIDA.md)

## 🌐 Despliegue

Para desplegar el proyecto en producción:

1. **Local:** Sigue [PRODUCCION.md](./setup/PRODUCCION.md)
2. **Cloud (Render):** Consulta [RENDER_DESPLIEGUE.md](./setup/RENDER_DESPLIEGUE.md)

## 📧 Funcionalidades de Notificación

El proyecto incluye sistema de notificaciones:

- **SMS (Twilio):** [TWILIO_CONFIGURACION.md](./setup/TWILIO_CONFIGURACION.md)
- **Email (SMTP):** [EMAIL_CONFIGURACION.md](./setup/EMAIL_CONFIGURACION.md)

## 🛠️ Tecnologías Principales

- **Framework:** Django 5.2.6
- **Base de datos:** PostgreSQL (Producción) / SQLite (Desarrollo)
- **Web Scraping:** Selenium + BeautifulSoup
- **SMS:** Twilio API
- **Email:** SMTP (Gmail)
- **Despliegue:** Render (Cloud Platform)
- **Servidor:** Gunicorn
- **Archivos Estáticos:** WhiteNoise

## 📝 Contribuir

Para contribuir al proyecto:

1. Revisar [CHECKLIST_GITHUB.md](./desarrollo/CHECKLIST_GITHUB.md)
2. Seguir las convenciones del equipo en [RESUMEN_EQUIPO.md](./equipo/RESUMEN_EQUIPO.md)
3. Ejecutar tests antes de hacer commit: [TESTS_RUN.md](./guias/TESTS_RUN.md)

## 📞 Soporte

Para dudas o problemas:

- Revisar la documentación correspondiente
- Consultar los logs del sistema
- Contactar con el equipo de desarrollo

---

**Última actualización:** Noviembre 2025  
**Versión del proyecto:** 1.0  
**Equipo:** Artemis IT Company
