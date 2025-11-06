#!/usr/bin/env python
"""
Script para convertir el logo correcto de Natursur a favicon.ico
Utiliza la imagen PNG más reciente como fuente
"""

import os
from PIL import Image
import tempfile
import shutil

# Obtener la imagen correcta (más reciente)
temp_dir = tempfile.gettempdir()
files = []
for f in os.listdir(temp_dir):
    if f.startswith('94bd9b1b-434d-4139-a769-01123a1f5238') and f.endswith('.tmp.png'):
        full_path = os.path.join(temp_dir, f)
        files.append((full_path, os.path.getctime(full_path)))

if not files:
    # Buscar por el patrón más reciente
    search_patterns = ['94bd9b1b', 'd6fff6b4']
    for pattern in search_patterns:
        for f in os.listdir(temp_dir):
            if pattern in f and f.endswith('.png'):
                full_path = os.path.join(temp_dir, f)
                files.append((full_path, os.path.getctime(full_path)))

if files:
    files.sort(key=lambda x: x[1], reverse=True)
    image_path = files[0][0]
else:
    print("❌ No se encontró la imagen del logo de Natursur")
    exit(1)

try:
    # Abrir imagen
    img = Image.open(image_path)
    print(f"✅ Imagen encontrada: {img.format} - {img.size}")
    
    # Convertir a RGB si es necesario
    if img.mode in ('RGBA', 'LA', 'P'):
        # Crear fondo blanco para transparencias
        bg = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = bg
    
    # Redimensionar a 256x256 (mejor calidad para favicon)
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    
    # Crear favicon con múltiples tamaños
    output_path = os.path.join(os.path.dirname(__file__), 'favicon.ico')
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    # Guardar como favicon.ico (multi-tamaño)
    img.save(output_path, format='ICO', sizes=sizes)
    print(f"✅ favicon.ico creado exitosamente ({os.path.getsize(output_path)} bytes)")
    
    # Guardar también el PNG como referencia con el nombre correcto
    png_output = os.path.join(os.path.dirname(__file__), 'natursur_logo_correcto.png')
    img.save(png_output, format='PNG')
    print(f"✅ natursur_logo_correcto.png guardado ({os.path.getsize(png_output)} bytes)")
    
    print("\n🎨 Logo oficial de Natursur integrado correctamente")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
