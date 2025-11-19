# Ejecutar tests (Django)

Instrucciones rápidas para ejecutar la suite de tests del proyecto (Windows / PowerShell):

1. Activar entorno virtual (si existe):

```powershell
cd "c:\Users\anton\OneDrive\Escritorio\Proyecto-PGPI"
# Ejecutar tests (Django)

Instrucciones rápidas para ejecutar la suite de tests del proyecto (Windows / PowerShell).

Requisitos previos:

- Tener un entorno virtual activado (recomendado).
- Haber aplicado migraciones (`python manage.py migrate`) antes de ejecutar la suite por primera vez.

Activar entorno virtual (ejemplo PowerShell):

```powershell
cd "c:\Users\anton\OneDrive\Escritorio\Proyecto-PGPI"
.\venv\Scripts\Activate.ps1
```

Instalar dependencias (si no están instaladas):

```powershell
pip install -r requirements.txt
```

Ejecutar todos los tests de Django:

```powershell
cd tienda_virtual
python manage.py test
```

Ejecutar tests de un módulo concreto (ejemplos):

```powershell
# ejecutar solo los tests de autenticación
python manage.py test home.test_auth

# ejecutar solo los tests de appointments
python manage.py test home.test_appointments

# ejecutar solo los tests de forms
python manage.py test home.test_forms

# ejecutar solo los tests de models
python manage.py test home.test_models
```

Ejecutar una prueba individual (ejemplo):

```powershell
python manage.py test home.tests.HomeAppTests.test_register_creates_user_and_securityprofile_and_autologin
```

Nuevas pruebas añadidas (resumen)

- `home/test_appointments.py`:
	- Verifica que no se puedan crear citas con fechas pasadas (server-side).
	- Comprueba que la vista de listado de citas requiere autenticación (redirección a login).
	- Crea una cita en el futuro y verifica que aparece en el listado.

- `home/test_forms.py`:
	- Comprueba la validación de `AppointmentForm.clean_datetime`: rechaza datetimes pasados y acepta datetimes futuros.

- `home/test_models.py`:
	- Comprueba la representación en string (`__str__`) del modelo `Appointment` y una comprobación básica de que la fecha de la cita es futura.

Notas y consideraciones importantes

- Las pruebas en `home/test_appointments.py` asumen que las URLs nombradas usadas en vistas son `home:citas_create` y `home:citas_list`. Si tus `urls.py` usan otros `name` distintos, actualiza los tests o ajusta los nombres en `urls.py`.
- El test que valida el rechazo de fechas pasadas busca en la respuesta la cadena de error en español: "La fecha y hora deben ser en el futuro". Si tu mensaje de `ValidationError` difiere, hay dos opciones:
	1. Cambiar el mensaje en el formulario para mantener coherencia con los tests.
	2. Modificar la aserción en el test para comprobar la existencia de errores en el campo (`self.assertIn('datetime', form.errors)`) en lugar de buscar texto exacto.
- Las pruebas no requieren dependencias de librerías frontend (p. ej. flatpickr) porque ejercitan la lógica del servidor y los formularios.
- Django crea una base de datos temporal para los tests; esto no modifica tu base de datos de desarrollo.
- Si los tests fallan por problemas de zona horaria, revisa `TIME_ZONE` y `USE_TZ` en `tienda_virtual/tienda_virtual/settings.py`.

Solución de problemas rápida

- Error de migraciones: ejecutar `python manage.py migrate`.
- Error de importación de módulos: asegurarse de ejecutar `python` desde el entorno virtual con las dependencias instaladas.
- Nombres de rutas diferentes: editar los tests para usar los nombres correctos o revisar `home/urls.py`.

¿Quieres que ejecute la suite de tests aquí y te presente el resultado? Si sí, lo ejecuto y corrijo fallos relacionados con mensajes de error o nombres de rutas.
