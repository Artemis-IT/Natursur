# Guía Rápida: Productos Herbalife

## ⚡ Inicio Rápido

### 1. Ejecutar el scraping

```powershell
cd tienda_virtual
python manage.py scrape_herbalife --max-clicks=10
```

### 2. Ver los productos

Abre tu navegador y navega a:

```
http://127.0.0.1:8000/productos/
```

O haz clic en "Catálogo Herbalife" desde la página principal.

### 3. Gestionar productos (opcional)

Accede al admin de Django:

```
http://127.0.0.1:8000/admin/home/product/
```

## 📋 Comandos útiles

### Scraping completo (borra productos anteriores)

```powershell
python manage.py scrape_herbalife --clear --max-clicks=15
```

### Scraping rápido (solo 5 clics)

```powershell
python manage.py scrape_herbalife --max-clicks=5
```

### Ver ayuda del comando

```powershell
python manage.py scrape_herbalife --help
```

## 🔍 Características

✅ Scraping automático de productos Herbalife  
✅ Almacenamiento en base de datos  
✅ Búsqueda por nombre de producto  
✅ Enlaces directos a la web de Herbalife  
✅ Grid responsive con imágenes  
✅ Gestión desde el admin de Django  

## 📝 Notas

- El scraping puede tardar 2-5 minutos dependiendo del número de clics
- Se requiere Chrome instalado en el sistema
- Los productos con `is_active=False` no se muestran en la web
- Puedes ejecutar el scraping varias veces; los productos se actualizan automáticamente

## 📚 Documentación completa

Ver `SCRAPING_PRODUCTOS.md` para documentación detallada.
