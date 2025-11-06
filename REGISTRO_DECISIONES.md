# REGISTRO DE DECISIONES - Proyecto Natursur

## Decisiones Técnicas y de Gestión del Proyecto

| ID | DECISIÓN | RESPONSABLE | FECHA |
|----|----------|-------------|-------|
| D-001 | Usar Django 5.2.6 como framework web principal | Tech Lead | 06/11/2025 |
| D-002 | Implementar autenticación dual: contraseña y pregunta de seguridad | Security Architect | 06/11/2025 |
| D-003 | Utilizar email como identificador único de usuario en lugar de username | UX Lead | 06/11/2025 |
| D-004 | Almacenar respuestas de seguridad hasheadas usando make_password de Django | Security Team | 06/11/2025 |
| D-005 | Crear aplicación 'home' como módulo principal del proyecto | Tech Lead | 06/11/2025 |
| D-006 | Usar SQLite como base de datos para desarrollo inicial | Database Admin | 06/11/2025 |
| D-007 | Implementar sistema de mensajes (messages framework) para feedback al usuario | UX Team | 06/11/2025 |
| D-008 | Mantener DEBUG=True durante fase de desarrollo | DevOps Lead | 06/11/2025 |
| D-009 | Usar plantillas HTML con herencia de Django para consistencia visual | Frontend Lead | 06/11/2025 |
| D-010 | Implementar decorador @login_required para proteger vistas de citas | Security Team | 06/11/2025 |
| D-011 | Auto-login después del registro para mejorar UX | Product Owner | 06/11/2025 |
| D-012 | Ordenar citas por fecha descendente en listado | Product Owner | 06/11/2025 |
| D-013 | Incluir campos first_name y last_name en registro de usuarios | UX Team | 06/11/2025 |
| D-014 | Usar OneToOneField para relación User-SecurityProfile | Database Architect | 06/11/2025 |
| D-015 | Proporcionar 12 preguntas de seguridad predefinidas en español | Content Team | 06/11/2025 |
| D-016 | Implementar método check_answer en SecurityProfile para validación | Tech Lead | 06/11/2025 |
| D-017 | Usar transaction.atomic para garantizar integridad en registro de usuario | Database Admin | 06/11/2025 |
| D-018 | Redirigir a login después de logout exitoso | UX Team | 06/11/2025 |
| D-019 | Permitir notas opcionales en modelo Appointment (blank=True) | Product Owner | 06/11/2025 |
| D-020 | Usar formato ISO para fechas en formularios de citas | UX Lead | 06/11/2025 |
| D-021 | Desarrollo rápido usando ChatGPT como herramienta de asistencia | Project Manager | 06/11/2025 |
| D-022 | Priorizar funcionalidad sobre testing en fase inicial | Project Manager | 06/11/2025 |
| D-023 | Postergar configuración de producción para fase posterior | DevOps Lead | 06/11/2025 |
| D-024 | No implementar recuperación de contraseña por email en MVP | Product Owner | 06/11/2025 |
| D-025 | Usar CSS personalizado en lugar de framework CSS | Frontend Lead | 06/11/2025 |

---

## Decisiones Pendientes de Revisión

| ID | DECISIÓN PENDIENTE | RESPONSABLE | FECHA LÍMITE |
|----|-------------------|-------------|--------------|
| DP-001 | Seleccionar base de datos para producción (PostgreSQL vs MySQL) | Database Admin | 13/11/2025 |
| DP-002 | Definir estrategia de despliegue (cloud provider y configuración) | DevOps Lead | 15/11/2025 |
| DP-003 | Establecer política de backup y recuperación de datos | Infrastructure Team | 20/11/2025 |
| DP-004 | Definir proceso de CI/CD para automatización | DevOps Team | 18/11/2025 |
| DP-005 | Seleccionar herramienta de monitoreo y logging | Operations Team | 22/11/2025 |

---

## Contexto del Proyecto

**Proyecto:** Sistema de gestión de citas y tienda virtual Natursur  
**Enfoque:** Desarrollo rápido mediante IA (ChatGPT)  
**Fase actual:** MVP - Desarrollo inicial  
**Metodología:** Desarrollo ágil iterativo  

---

**Fecha de creación del registro:** 06/11/2025  
**Responsable del registro:** Project Manager  
**Última actualización:** 06/11/2025  
**Próxima revisión:** 13/11/2025
