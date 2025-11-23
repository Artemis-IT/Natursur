# Instrucciones de Instalación - Actualización

## Para nuevos desarrolladores o después de hacer `git pull`

Si acabas de clonar el repositorio o has hecho `git pull` y hay cambios en `requirements.txt`, sigue estos pasos:

### 1. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
cd Proyecto-PGPI
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
cd Proyecto-PGPI
source venv/bin/activate
```

### 2. Actualizar dependencias

```bash
pip install -r requirements.txt --upgrade
```

### 3. Aplicar migraciones (si las hay)

```bash
cd tienda_virtual
python manage.py migrate
```

### 4. Verificar la instalación

Ejecutar las pruebas para asegurarse de que todo funciona:

```bash
python manage.py test home.tests
```

**Resultado esperado:**
```
Ran 48 tests in ~110s
OK
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## Paquetes Nuevos Añadidos

Los siguientes paquetes se han actualizado/añadido para soportar las **48 pruebas unitarias**:

- `python-dotenv==1.2.1` (actualizado de 1.0.0)
- `dj-database-url==3.0.1` (actualizado de 1.2.0)
- `psycopg2-binary==2.9.11` (actualizado de 2.9.7)
- `twilio==9.8.6` (especificada versión)

Estos paquetes son necesarios para:
- ✅ Pruebas de envío de SMS (Twilio)
- ✅ Pruebas de envío de Email
- ✅ Pruebas del carrito
- ✅ Pruebas de modelos y formularios

---

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'dotenv'"

**Solución:**
```bash
pip install python-dotenv==1.2.1
```

### Error: "ModuleNotFoundError: No module named 'twilio'"

**Solución:**
```bash
pip install twilio==9.8.6
```

### Las pruebas fallan

**Solución:**
1. Asegúrate de tener el entorno virtual activado
2. Reinstala todas las dependencias:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```
3. Ejecuta las migraciones:
   ```bash
   python manage.py migrate
   ```

---

## Verificación Rápida

Ejecuta este comando para verificar que todo está OK:

```bash
python manage.py check && python manage.py test home.tests
```

Si ves `OK` en ambos comandos, ¡todo está funcionando correctamente! ✅

---

**Fecha de actualización:** Noviembre 2025  
**Cambios principales:** Añadidas 48 pruebas unitarias y actualizadas dependencias
