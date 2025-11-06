# REGISTRO DE INCIDENCIAS - Proyecto Natursur

## Tabla de Incidencias

| ID DEL INCIDENTE | FECHA DE OCURRENCIA | CATEGORÍA | INCIDENTE / PROBLEMA | INVOLUCRADOS | IMPACTO | URGENCIA |
|------------------|---------------------|-----------|----------------------|--------------|---------|----------|
| 1 | 06/11/2025 | Seguridad | SECRET_KEY expuesta en settings.py en modo DEBUG=True | Equipo de desarrollo | Alto - Riesgo de seguridad en producción | Alta |
| 2 | 06/11/2025 | Configuración | ALLOWED_HOSTS vacío, limitando despliegue en producción | Equipo DevOps | Medio - Bloquea despliegue | Media |
| 3 | 06/11/2025 | Base de datos | Falta configuración de base de datos de producción (usando SQLite por defecto) | Equipo de infraestructura | Medio - No escalable | Media |
| 4 | 06/11/2025 | Seguridad | Falta implementación de HTTPS y configuraciones de seguridad para producción | Equipo de seguridad | Alto - Datos no encriptados en tránsito | Alta |
| 5 | 06/11/2025 | Validación | Falta validación de fechas pasadas en modelo Appointment | Equipo de desarrollo | Bajo - Permite citas en fechas pasadas | Baja |
| 6 | 06/11/2025 | Dependencias | requirements.txt solo incluye Django, faltan dependencias adicionales | Equipo de desarrollo | Bajo - Instalación incompleta | Baja |
| 7 | 06/11/2025 | Testing | No hay tests implementados para validar funcionalidad | Equipo QA | Medio - Sin garantía de calidad | Media |

## Tabla de Seguimiento

| ID DEL INCIDENTE | PROPIETARIO | FECHA DE VENCIMIENTO | ESTADO | FECHA DE SOLUCIÓN | ACCIONES TOMADAS | COMENTARIOS |
|------------------|-------------|----------------------|--------|-------------------|------------------|-------------|
| 1 | DevOps Lead | 08/11/2025 | Pendiente | - | Configurar variables de entorno para SECRET_KEY y DEBUG | Crítico para producción |
| 2 | DevOps Lead | 08/11/2025 | Pendiente | - | Actualizar ALLOWED_HOSTS con dominios de producción | Coordinar con infraestructura |
| 3 | Database Admin | 13/11/2025 | Pendiente | - | Configurar PostgreSQL o MySQL para producción | Migración de datos necesaria |
| 4 | Security Team | 10/11/2025 | Pendiente | - | Implementar SSL/TLS, SECURE_SSL_REDIRECT, HSTS | Requiere certificado SSL |
| 5 | Backend Developer | 09/11/2025 | Pendiente | - | Agregar validación en formulario y modelo para fechas futuras | Mejora de UX |
| 6 | DevOps Lead | 07/11/2025 | Pendiente | - | Agregar pillow, gunicorn, psycopg2 a requirements.txt | Revisar dependencias completas |
| 7 | QA Lead | 15/11/2025 | Pendiente | - | Crear suite de tests unitarios e integración | Implementar CI/CD |

---

**Fecha de creación del registro:** 06/11/2025  
**Responsable del registro:** Project Manager  
**Última actualización:** 06/11/2025
