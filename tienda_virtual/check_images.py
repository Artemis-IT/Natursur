import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_virtual.settings')
django.setup()

from home.models import Product

total = Product.objects.count()
con_imagen = Product.objects.exclude(image_url__isnull=True).exclude(image_url='').count()
sin_imagen = total - con_imagen

print(f"Total productos: {total}")
print(f"Con imagen: {con_imagen}")
print(f"Sin imagen: {sin_imagen}")
print("\nEjemplos de productos:")

for p in Product.objects.all()[:5]:
    img_status = "✓ SÍ" if p.image_url else "✗ NO"
    print(f"  {img_status} | {p.name[:50]}")
    if p.image_url:
        print(f"      {p.image_url[:80]}")
