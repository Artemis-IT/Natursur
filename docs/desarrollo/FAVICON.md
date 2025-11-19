# 🎨 Favicon - Logo de Natursur

## ✅ Archivos Creados

```
✅ favicon.ico                      - Icono multi-tamaño para navegador
✅ natursur_logo.png                - Logo original de Natursur (referencia)
✅ create_favicon_from_image.py     - Script para regenerar desde imagen
```

## 📍 Ubicación

```
tienda_virtual/home/static/
├── favicon.ico                  ← Icono del navegador (¡aquí!)
├── natursur_logo.png            ← Logo original de Natursur
├── favicon.svg                  ← Versión SVG (alternativa)
└── css/
    └── styles.css
```

## 🎯 Características

**Diseño:**
- Logo original de Natursur (hoja y sol)
- Colores corporativos profesionales
- Imagen reconocible y de alta calidad
- Escalable a cualquier tamaño

**Tamaños incluidos:**
- 16 px (pestaña del navegador)
- 32 px (acceso directo)
- 48 px (barra de herramientas)
- 64 px (icono ampliado)
- 128 px (marcadores)
- 256 px (máxima resolución)

## 📱 Dónde Aparece

```
✅ Pestaña del navegador (parte superior)
✅ Bookmarks / Favoritos
✅ Historial del navegador
✅ Accesos directos del escritorio
✅ Feeds RSS
✅ Pantalla de inicio (web apps)
```

## 🔧 Integración en Templates

El favicon está vinculado en todas las plantillas HTML:

```html
<link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
```

**Plantillas actualizadas:**
- ✅ index.html (landing page)
- ✅ register.html (registro)
- ✅ login.html (login)
- ✅ appointments.html (listado de citas)
- ✅ appointment_form.html (nueva cita)

## 🔄 Regenerar Favicon

Si quieres cambiar el diseño del favicon:

### Opción 1: Editar SVG y regenerar

```bash
# 1. Editar favicon.svg en editor de imágenes
# 2. Ejecutar script
python create_favicon.py
```

### Opción 2: Cambiar colores en create_favicon.py

En el archivo `create_favicon.py`, línea ~30:

```python
GREEN_PRIMARY = (42, 157, 143, 255)      # #2a9d8f
GREEN_DARK = (31, 112, 102, 255)         # #1f7066
WHITE = (255, 255, 255, 255)
```

Luego ejecutar:

```bash
python create_favicon.py
```

### Opción 3: Desde imagen externa

Si tienes una imagen PNG:

```python
from PIL import Image

img = Image.open("mi_logo.png")
img = img.resize((256, 256))
img.save("favicon.ico", format="ICO")
```

## 📊 Especificaciones Técnicas

```
Formato:           ICO (multi-tamaño)
Versión:           v1.0
Codificación:      32-bit RGBA
Transparencia:     Sí (fondo transparente)
Compatibilidad:    Todos los navegadores modernos
Peso:              ~3 KB
```

## 🌐 Compatibilidad

```
✅ Chrome              ✅ Safari
✅ Firefox             ✅ Opera
✅ Edge                ✅ Internet Explorer (11+)
✅ iOS Safari          ✅ Android Chrome
✅ Android Firefox     ✅ Samsung Internet
```

## 🎨 Alternativas de Diseño

### Si quieres cambiar:

1. **Color principal:** Editar `GREEN_PRIMARY` en create_favicon.py
2. **Forma:** Editar las coordenadas en `leaf_points[]`
3. **Detalles:** Agregar más líneas con `draw.line()` o círculos con `draw.ellipse()`

## 📥 Caché del Navegador

El favicon puede estar en caché. Para verlo actualizado:

```html
<!-- Forzar actualización agregando versión -->
<link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}?v=1.1">
```

## ✨ Resultado

Cuando abras el navegador verás:
- Pestaña con el icono de Natursur (hoja verde)
- En favoritos aparecerá el mismo icono
- En accesos directos será visible

## 🛠️ Si Necesitas Cambiar

```bash
# 1. Editar create_favicon.py
# 2. Ejecutar:
python create_favicon.py

# 3. Limpiar caché del navegador:
# Ctrl+Shift+Delete (Chrome/Firefox)

# 4. Recargar página:
# Ctrl+Shift+R (fuerza recarga sin caché)
```

## 📝 Archivos Relacionados

- `create_favicon.py` - Script Python (puedes editarlo)
- `favicon.svg` - Versión vectorial original
- `favicon.ico` - Icono compilado (¡NO editar!)
- `home/templates/*/html` - Templates con referencia

---

**¡Favicon listo para usar!** 🌿
