#!/usr/bin/env python3
"""
Script para generar favicon.ico desde SVG
Requiere: pip install Pillow
"""

from PIL import Image, ImageDraw
import io

def create_favicon_ico():
    """Crea un favicon.ico con el logo de Natursur"""
    
    # Crear imagen con fondo blanco
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Color principal (verde Natursur)
    GREEN_PRIMARY = (42, 157, 143, 255)      # #2a9d8f
    GREEN_DARK = (31, 112, 102, 255)         # #1f7066
    WHITE = (255, 255, 255, 255)
    
    # Centro de la imagen
    center = size // 2
    
    # Dibujar círculo de fondo
    radius = 110
    bbox = [center - radius, center - radius, center + radius, center + radius]
    draw.ellipse(bbox, fill=GREEN_PRIMARY, outline=GREEN_DARK, width=2)
    
    # Dibujar hoja (símbolo de nutrición)
    # Hoja blanca
    leaf_points = [
        (center, center - 60),      # Punta superior
        (center + 40, center - 25), # Derecha superior
        (center + 50, center),      # Derecha media
        (center + 40, center + 25), # Derecha inferior
        (center, center + 45),      # Punta inferior
        (center - 40, center + 25), # Izquierda inferior
        (center - 50, center),      # Izquierda media
        (center - 40, center - 25), # Izquierda superior
    ]
    draw.polygon(leaf_points, fill=WHITE, outline=None)
    
    # Vena central
    draw.line(
        [(center, center - 60), (center, center + 45)],
        fill=GREEN_PRIMARY,
        width=2
    )
    
    # Venas laterales izquierdas
    draw.line([(center - 10, center - 40), (center - 30, center)], fill=GREEN_PRIMARY, width=1)
    draw.line([(center - 20, center + 20), (center - 25, center + 35)], fill=GREEN_PRIMARY, width=1)
    
    # Venas laterales derechas
    draw.line([(center + 10, center - 40), (center + 30, center)], fill=GREEN_PRIMARY, width=1)
    draw.line([(center + 20, center + 20), (center + 25, center + 35)], fill=GREEN_PRIMARY, width=1)
    
    # Detalles decorativos
    detail_color = (255, 255, 255, 128)
    draw.ellipse([center - 60, center + 65, center - 45, center + 80], fill=detail_color)
    draw.ellipse([center + 45, center + 65, center + 60, center + 80], fill=detail_color)
    
    # Guardar como ICO en diferentes tamaños
    output_path = r"c:\Users\aleja\OneDrive\Escritorio\BAKOP\COSITAS CARRERA\4to\PGPI\proyecto\tienda_virtual\home\static\favicon.ico"
    
    # Crear múltiples versiones para diferentes tamaños
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        images.append(resized)
    
    # Guardar como ICO (usa la versión más grande como principal)
    images[0].save(
        output_path,
        format='ICO',
        sizes=[(size, size) for size in sizes]
    )
    
    print(f"✅ favicon.ico creado correctamente en:")
    print(f"   {output_path}")
    print(f"\n✨ Favicon creado con logo de Natursur (hoja verde)")
    print(f"   Tamaños incluidos: {', '.join(map(str, sizes))} px")

if __name__ == "__main__":
    create_favicon_ico()
