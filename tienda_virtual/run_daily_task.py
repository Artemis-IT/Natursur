# *** ESTA ES LA PARTE IMPORTANTE ***
# Añadir la raíz del proyecto al PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from tienda_virtual.home.send_mail import send_daily_order_summary

#!/usr/bin/env python
"""Script para ejecutar la tarea diaria de envío de emails"""
import os
import sys
import django

# Configurar el path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_virtual.settings')
django.setup()


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