#!/usr/bin/env python
"""Script para ejecutar la tarea diaria de envío de emails"""
import os
import sys
import django

# Configurar el path - BASE_DIR es el directorio donde está este script (tienda_virtual/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Cambiar al directorio base para asegurar que las rutas funcionen
os.chdir(BASE_DIR)
sys.path.insert(0, BASE_DIR)

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_virtual.settings')
django.setup()

# Importar la función
from home.send_mail import send_daily_order_summary

if __name__ == '__main__':
    try:
        print("Iniciando envío de resumen diario de pedidos...")
        result = send_daily_order_summary()
        print(f"Tarea completada exitosamente: {result}")
    except Exception as e:
        print(f"Error al ejecutar tarea: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)