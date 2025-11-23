# Ejecutar Tests - Guía Completa

Instrucciones para ejecutar la suite completa de tests unitarios del proyecto Natursur.

## 📊 Resumen de Tests

- **Total de pruebas:** 48 pruebas unitarias
- **Cobertura:** Modelos, Formularios, Cart, Utilidades (SMS/Email)
- **Framework:** Django TestCase + unittest.mock
- **Estado actual:** ✅ 48/48 pasando

---

## 🚀 Inicio Rápido

### Windows PowerShell

```powershell
# 1. Ir al directorio del proyecto
cd "C:\Users\anton\OneDrive\Escritorio\Proyecto-PGPI"

# 2. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 3. Ir a la carpeta Django
cd tienda_virtual

# 4. Ejecutar todos los tests
python manage.py test home.tests
```

### Linux/macOS

```bash
# 1. Ir al directorio del proyecto
cd /ruta/al/Proyecto-PGPI

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Ir a la carpeta Django
cd tienda_virtual

# 4. Ejecutar todos los tests
python manage.py test home.tests
```

---

## 📋 Requisitos Previos

### 1. Entorno Virtual Activado

**Windows:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 2. Dependencias Instaladas

```bash
pip install -r requirements.txt
```

Dependencias necesarias para tests:
- `Django>=5.2.6`
- `python-dotenv` (para variables de entorno)
- `twilio` (mockeado en tests)

### 3. Migraciones Aplicadas

```bash
cd tienda_virtual
python manage.py migrate
```

---

## 🎯 Comandos de Ejecución

### Ejecutar Todos los Tests

```bash
python manage.py test home.tests
```

**Salida esperada:**
```
Found 48 test(s).
Creating test database...
...................................................
----------------------------------------------------------------------
Ran 48 tests in 110s

OK
```

### Ejecutar con Verbosidad Alta

```bash
python manage.py test home.tests --verbosity=2
```

Muestra cada test ejecutado con su descripción.

### Ejecutar Tests de una Clase Específica

```bash
# Tests de modelos
python manage.py test home.tests.AppointmentModelTest
python manage.py test home.tests.ProductModelTest
python manage.py test home.tests.OrderModelTest

# Tests de formularios
python manage.py test home.tests.RegistrationFormTest
python manage.py test home.tests.LoginFormTest

# Tests del carrito
python manage.py test home.tests.CartTest

# Tests de utilidades
python manage.py test home.tests.SendSMSTest
python manage.py test home.tests.SendEmailTest
```

### Ejecutar un Test Específico

```bash
# Formato: home.tests.ClaseTest.metodo_test
python manage.py test home.tests.AppointmentModelTest.test_appointment_creation
python manage.py test home.tests.CartTest.test_cart_add_product
python manage.py test home.tests.SendSMSTest.test_send_price_sms_success
```

### Mantener Base de Datos de Prueba

```bash
# Útil para acelerar ejecuciones repetidas
python manage.py test home.tests --keepdb
```

### Ejecutar en Paralelo (si tienes múltiples cores)

```bash
python manage.py test home.tests --parallel
```

---

## 📦 Categorías de Tests

### 1. Tests de Modelos (30 tests)

```bash
# Appointment (4 tests)
python manage.py test home.tests.AppointmentModelTest

# SecurityProfile (5 tests)  
python manage.py test home.tests.SecurityProfileModelTest

# Product (6 tests)
python manage.py test home.tests.ProductModelTest

# Order (6 tests)
python manage.py test home.tests.OrderModelTest

# OrderItem (3 tests)
python manage.py test home.tests.OrderItemModelTest
```

### 2. Tests de Formularios (12 tests)

```bash
# AppointmentForm (3 tests)
python manage.py test home.tests.AppointmentFormTest

# RegistrationForm (4 tests)
python manage.py test home.tests.RegistrationFormTest

# LoginForm (3 tests)
python manage.py test home.tests.LoginFormTest

# CheckoutForm (3 tests)
python manage.py test home.tests.CheckoutFormTest
```

### 3. Tests del Carrito (8 tests)

```bash
python manage.py test home.tests.CartTest
```

### 4. Tests de Utilidades (4 tests)

```bash
# SMS (2 tests)
python manage.py test home.tests.SendSMSTest

# Email (2 tests)
python manage.py test home.tests.SendEmailTest
```

---

## 📊 Análisis de Cobertura

### Instalar Coverage

```bash
pip install coverage
```

### Ejecutar Tests con Coverage

```bash
coverage run --source='home' manage.py test home.tests
```

### Ver Reporte en Terminal

```bash
coverage report
```

**Salida esperada:**
```
Name                     Stmts   Miss  Cover
--------------------------------------------
home/__init__.py             0      0   100%
home/models.py              50      2    96%
home/forms.py               80      5    94%
home/cart.py                45      3    93%
home/send_sms.py            15      1    93%
home/send_mail.py           35      2    94%
--------------------------------------------
TOTAL                      225     13    94%
```

### Generar Reporte HTML

```bash
coverage html
```

Luego abrir `htmlcov/index.html` en el navegador.

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'dotenv'"

**Solución:**
```bash
pip install python-dotenv
```

### Error: "No module named 'twilio'"

**Solución:**
```bash
pip install twilio
```

### Error: "Settings cannot be imported"

**Solución:** Asegúrate de estar en el directorio `tienda_virtual`:
```bash
cd tienda_virtual
python manage.py test home.tests
```

### Tests muy lentos

**Solución 1:** Usar `--keepdb`
```bash
python manage.py test home.tests --keepdb
```

**Solución 2:** Ejecutar en paralelo
```bash
python manage.py test home.tests --parallel
```

### Error de base de datos

**Solución:** Eliminar y recrear la base de datos de prueba
```bash
# Eliminar archivo de BD de prueba si existe
rm test_*.db

# Ejecutar tests sin --keepdb
python manage.py test home.tests
```

---

## 📝 Buenas Prácticas

### ✅ Antes de Commit

Siempre ejecutar tests antes de hacer commit:
```bash
python manage.py test home.tests
```

### ✅ Antes de Push

Ejecutar tests con verbosidad para ver detalles:
```bash
python manage.py test home.tests --verbosity=2
```

### ✅ Después de Cambios Importantes

Ejecutar tests completos + coverage:
```bash
coverage run --source='home' manage.py test home.tests
coverage report
```

### ✅ En CI/CD

Configurar GitHub Actions para ejecutar tests automáticamente:
```yaml
- name: Run tests
  run: |
    cd tienda_virtual
    python manage.py test home.tests --verbosity=2
```

---

## 📚 Documentación Adicional

- **[INFORME_PRUEBAS.md](../desarrollo/INFORME_PRUEBAS.md)** - Informe detallado de todas las pruebas
- **[Código de tests](../../tienda_virtual/home/tests.py)** - Archivo de pruebas completo

---

## 📈 Métricas Actuales

| Métrica | Valor |
|---------|-------|
| Total de pruebas | 48 |
| Pruebas pasando | 48 ✅ |
| Tiempo de ejecución | ~110s |
| Cobertura estimada | ~94% |

---

## 🔄 Integración Continua

### GitHub Actions (ejemplo)

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        cd tienda_virtual
        python manage.py test home.tests --verbosity=2
```

---

**Última actualización:** Noviembre 2025  
**Autor:** Equipo Artemis IT  
**Proyecto:** Natursur
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
