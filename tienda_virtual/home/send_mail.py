from django.utils import timezone
from django.core.mail import EmailMessage
from home.models import Order


def send_daily_order_summary():
    today = timezone.localdate()
    
    orders_today = Order.objects.filter(created_at__date=today)
    
    if orders_today.exists():
        
        # Encabezado
        body = "=" * 60 + "\n"
        body += "        RESUMEN DIARIO DE PEDIDOS\n"
        body += f"        {today.strftime('%d/%m/%Y')}\n"
        body += "=" * 60 + "\n\n"
        body += f"Total de pedidos recibidos: {orders_today.count()}\n"
        body += "=" * 60 + "\n\n"
        
        # Procesar cada pedido
        for idx, order in enumerate(orders_today, start=1):
            print(f"[DEBUG] Procesando pedido ID: {order.id}")
            
            body += f"PEDIDO #{idx}\n"
            body += f"Numero de Seguimiento: {order.id}\n"
            body += "-" * 60 + "\n\n"
            
            # Artículos
            body += "ARTICULOS:\n"
            items = order.items.all()
            for item in items:
                body += f"  - {item.product_name} ........................ x{item.quantity}\n"
            
            body += "\n"
            
            # Datos del cliente
            body += "DATOS DEL CLIENTE:\n"
            body += f"  Nombre: {order.customer_name}\n"
            body += f"  Email: {order.customer_email}\n"
            
            if order.customer_phone:
                body += f"  Telefono: {order.customer_phone}\n"
            
            body += "\n"
            body += "DIRECCION DE ENTREGA:\n"
            body += f"  {order.delivery_address}\n"
            body += f"  {order.delivery_city}, CP: {order.delivery_postal_code}\n"
            
            if order.notes:
                body += "\nNOTAS:\n"
                body += f"  {order.notes}\n"
            
            body += "\n" + "=" * 60 + "\n\n"
        
        body += "\n" + "-" * 60 + "\n"
        body += "Este es un resumen automatico generado por Natursur\n"
        body += f"Fecha y hora de envio: {timezone.now().strftime('%d/%m/%Y %H:%M')}\n"
        
        print(f"[DEBUG] Body tiene {len(body)} caracteres")
    else:
        print(f"[DEBUG] Entrando en ELSE - No se encontraron pedidos")
        body = "=" * 60 + "\n"
        body += "        RESUMEN DIARIO DE PEDIDOS\n"
        body += f"        {today.strftime('%d/%m/%Y')}\n"
        body += "=" * 60 + "\n\n"
        body += "Hoy no se han registrado pedidos.\n"
    
    email = EmailMessage(
        subject=f"Resumen de pedidos del {today.strftime('%d/%m/%Y')}",
        body=body,
        from_email="artemisitcompany@gmail.com",
        to=["alecarrei1@alum.us.es"],
    )
    email.content_subtype = "plain"
    email.encoding = 'utf-8'
    email.send()
    
    print(f"[DEBUG] Email enviado")
    
    return f"Email enviado con {orders_today.count()} pedidos"