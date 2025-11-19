# Sistema de Scraping de Productos Herbalife

## Descripción

Este módulo permite scrapear productos de Herbalife desde su página oficial y mostrarlos en la web de Natursur con enlaces directos a las páginas originales de cada producto.

## Componentes

### 1. Modelo `Product` (`home/models.py`)

Modelo Django que almacena la información de los productos:

- **name**: Nombre del producto
- **herbalife_url**: URL original del producto en Herbalife (único)
- **image_url**: URL de la imagen del producto (opcional)
- **description**: Descripción del producto (opcional)
- **category**: Categoría del producto (opcional)
- **is_active**: Controla si el producto se muestra en la web
- **created_at**: Fecha de creación
- **updated_at**: Fecha de última actualización

### 2. Comando de Gestión `scrape_herbalife`

Ubicación: `home/management/commands/scrape_herbalife.py`

#### Uso básico

```powershell
python manage.py scrape_herbalife
```

#### Opciones disponibles

**`--max-clicks=N`**: Número de veces que se hace clic en "Carga más" (default: 10)

```powershell
python manage.py scrape_herbalife --max-clicks=20
```

**`--clear`**: Borra todos los productos existentes antes de scrapear

```powershell
python manage.py scrape_herbalife --clear
```

**Ejemplo combinado**:

```powershell
python manage.py scrape_herbalife --clear --max-clicks=15
```

#### Funcionamiento

1. Abre Chrome mediante Selenium
2. Navega a la página de todos los productos de Herbalife
3. Hace clic repetidamente en "Carga más" para cargar más productos
4. Extrae nombre, URL e imagen de cada producto
5. Guarda o actualiza productos en la base de datos
6. Muestra estadísticas al finalizar

### 3. Vista `products_list` (`home/views.py`)

Vista que muestra el catálogo de productos con funcionalidad de búsqueda.

**URL**: `/productos/`

**Características**:
- Muestra solo productos activos (`is_active=True`)
- Buscador por nombre de producto
- Grid responsive de productos
- Enlaces externos a Herbalife que abren en nueva pestaña

### 4. Template `products.html`

Template responsive con:
- Header con buscador integrado
- Grid de productos con imágenes
- Botones que redirigen a la web de Herbalife
- Placeholder visual para productos sin imagen
- Mensaje informativo si no hay productos

## Integración en la Web

### Enlaces añadidos

1. **Navegación principal** (`index.html`):
   - Enlace "Catálogo Herbalife" en el menú
   
2. **Hero section**:
   - Botón "🌿 Ver productos Herbalife" junto a "Empieza ahora"

### Admin de Django

El modelo `Product` está registrado en el admin (`/admin/`) con:
- Listado con filtros por categoría, estado y fecha
- Búsqueda por nombre y descripción
- Activación/desactivación rápida desde el listado
- Organización en fieldsets

## Flujo de Trabajo Recomendado

### Primera carga de productos

1. Asegúrate de tener Selenium y pandas instalados:

```powershell
pip install selenium pandas
```

2. Ejecuta el scraping inicial:

```powershell
python manage.py scrape_herbalife --clear --max-clicks=15
```

3. Verifica los productos en el admin o en `/productos/`

### Actualización periódica

Para actualizar el catálogo sin borrar productos existentes:

```powershell
python manage.py scrape_herbalife --max-clicks=10
```

Los productos existentes se actualizan; los nuevos se crean.

### Gestión manual

Desde el admin (`/admin/home/product/`):
- Editar nombres o descripciones
- Añadir categorías manualmente
- Activar/desactivar productos
- Eliminar productos obsoletos

## Requisitos del Sistema

### Dependencias Python

```
Django>=5.2
selenium>=4.0
pandas>=2.0
```

### ChromeDriver

El script de scraping requiere ChromeDriver compatible con tu versión de Chrome. Selenium lo gestiona automáticamente en versiones recientes.

### Navegador

Google Chrome instalado en el sistema.

## Notas Técnicas

### Seguridad

- Todos los enlaces a Herbalife incluyen `target="_blank"` y `rel="noopener noreferrer"` por seguridad
- El modelo usa `URLField` con validación de URLs

### Rendimiento

- El scraping puede tardar varios minutos dependiendo del número de clics
- Se recomienda ejecutarlo en horarios de bajo tráfico
- Los productos se guardan con `update_or_create` para evitar duplicados

### Personalización

Para modificar la web de origen o selectores CSS/XPath:
1. Edita `home/management/commands/scrape_herbalife.py`
2. Ajusta la URL en la línea: `url = "https://www.herbalife.com/es-es/u/category/all-products"`
3. Modifica los selectores XPath según la estructura de la página

## Troubleshooting

### Error: "ChromeDriver not found"

Instala ChromeDriver manualmente o actualiza Selenium:

```powershell
pip install --upgrade selenium
```

### No se encuentran productos

- Verifica que la URL de Herbalife sea correcta
- Revisa los selectores XPath en el comando
- Aumenta el tiempo de espera (`time.sleep`)

### Productos sin imagen

Es normal que algunos productos no tengan imagen. El template muestra un placeholder (🌱) en esos casos.

### El botón "Carga más" no se encuentra

La página puede haber cargado todos los productos. El script continúa automáticamente sin error.

## Mejoras Futuras

- [ ] Scraping de descripciones y precios
- [ ] Categorización automática de productos
- [ ] Programación de scraping automático (Celery/cron)
- [ ] Cache de imágenes localmente
- [ ] Sistema de favoritos para usuarios
- [ ] Comparador de productos

---

**Elaborado por**: Antonio Luis Jiménez de la Fuente (Project Manager) y el equipo de desarrollo de Natursur  
**Última actualización**: Noviembre 2025
