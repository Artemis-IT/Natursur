#!/usr/bin/env python3
"""
Crear favicon.ico desde imagen de Natursur
"""

from PIL import Image

# Usar la imagen de Natursur
img_path = r"C:\Users\aleja\AppData\Local\Temp\d6fff6b4-eea1-4ee8-b36d-6ae638e8f9c2.png"

try:
    # Abrir y procesar imagen
    img = Image.open(img_path)
    print(f"✅ Imagen encontrada: {img.format} - {img.size}")
    
    # Convertir a RGBA (por si tiene canal alpha)
    img = img.convert('RGBA')
    
    # Redimensionar a 256x256 (tamaño máximo)
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    
    # Crear múltiples tamaños
    sizes = [16, 32, 48, 64, 128, 256]
    images = [img.resize((s, s), Image.Resampling.LANCZOS) for s in sizes]
    
    # Guardar como favicon.ico
    output_path = r"tienda_virtual\home\static\favicon.ico"
    images[0].save(
        output_path,
        format='ICO',
        sizes=[(s, s) for s in sizes]
    )
    
    print(f"✅ favicon.ico creado exitosamente")
    print(f"📍 Ubicación: {output_path}")
    print(f"📊 Tamaños: {sizes}")
    
    # Guardar también PNG en static para referencia
    img.save(r"tienda_virtual\home\static\natursur_logo.png")
    print(f"✅ Logo PNG guardado también")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
