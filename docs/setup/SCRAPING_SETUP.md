# Guía de Inicialización del Scraping de Productos Herbalife

## Descripción
Este proyecto incluye un sistema de web scraping para obtener productos de Herbalife y almacenarlos en la base de datos.

## Requisitos Previos

1. **Entorno virtual activado**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Dependencias instaladas**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Google Chrome instalado** (el scraping usa Chrome WebDriver)

## Pasos para Ejecutar el Scraping

### Opción 1: Comando Django Manual

```powershell
cd tienda_virtual
python manage.py scrape_herbalife
```

### Opción 2: Script Automatizado

Ejecuta el script incluido que realiza todo el proceso:

```powershell
.\run_scraping.ps1
```

## ¿Qué hace el scraping?

1. **Accede** a la tienda online de Herbalife España
2. **Navega** automáticamente por todas las categorías de productos
3. **Extrae** información de cada producto:
   - Nombre del producto
   - URL de Herbalife
   - URL de la imagen
4. **Almacena** los productos en la base de datos (modelo `Product`)
5. **Actualiza** productos existentes si ya están en la base de datos

## Resultados Esperados

- **~88 productos** extraídos (puede variar según el catálogo de Herbalife)
- Tiempo estimado: **2-3 minutos**
- Los productos quedan disponibles en:
  - Página de inicio (3 productos destacados aleatorios)
  - `/products/` (listado completo con búsqueda)

## Verificar los Productos

Después del scraping, verifica que los productos se cargaron correctamente:

```powershell
cd tienda_virtual
python manage.py shell -c "from home.models import Product; print(f'Total productos: {Product.objects.count()}')"
```

## Solución de Problemas

### Error: "Chrome WebDriver not found"
**Solución:** El WebDriver se descarga automáticamente. Si falla, asegúrate de tener Chrome instalado.

### Error: "selenium module not found"
**Solución:** 
```powershell
pip install selenium
```

### Productos duplicados
**Solución:** El comando usa `update_or_create()`, así que puedes ejecutarlo múltiples veces sin crear duplicados.

### El scraping se detiene antes de tiempo
**Solución:** Algunos botones de categoría pueden tardar en cargar. El script tiene reintentos automáticos, pero si persiste el problema, ejecuta el comando nuevamente.

## Mantenimiento

Para actualizar los productos con los últimos del catálogo de Herbalife, simplemente vuelve a ejecutar:

```powershell
python manage.py scrape_herbalife
```

El sistema actualizará los productos existentes y añadirá los nuevos.

## Arquitectura del Scraping

- **Comando:** `tienda_virtual/home/management/commands/scrape_herbalife.py`
- **Modelo:** `tienda_virtual/home/models.py` (clase `Product`)
- **Tecnología:** Selenium WebDriver + Chrome
- **Estrategia:** Navegación dinámica con detección inteligente de botones y esperas adaptativas

## Notas Importantes

⚠️ **Base de datos local:** La base de datos (`db.sqlite3`) está en `.gitignore`, por lo que cada miembro del equipo debe ejecutar el scraping después de clonar el repositorio.

✅ **Idempotente:** Puedes ejecutar el scraping múltiples veces sin problemas.

📊 **Monitoreo:** El comando muestra en consola cada producto que va añadiendo.
