from django.utils import timezone
from django.core.mail import EmailMessage
from home.models import Order


def send_daily_order_summary():
    today = timezone.localdate()
    
    print(f"[DEBUG] Fecha buscada: {today}")
    
    orders_today = Order.objects.filter(created_at__date=today)
    
    print(f"[DEBUG] Pedidos encontrados: {orders_today.count()}")
    
    summaries = []
    
    if orders_today.exists():
        print(f"[DEBUG] Entrando en IF - orders_today.exists() = True")
        for order in orders_today:
            print(f"[DEBUG] Procesando pedido ID: {order.id}")
            summary = f"{order.get_items_summary()}\nPedido por {order.customer_name} a la direccion {order.delivery_address}"
            summaries.append(summary)
        
        body = "\n\n".join(summaries)
        print(f"[DEBUG] Body tiene {len(body)} caracteres")
    else:
        print(f"[DEBUG] Entrando en ELSE - No se encontraron pedidos")
        body = "Hoy no se han registrado pedidos."
    
    email = EmailMessage(
        subject=f"Resumen de pedidos del {today}",
        body=body,
        from_email="artemisitcompany@gmail.com",
        to=["alecarrei1@alum.us.es"],
    )
    email.content_subtype = "plain"
    email.encoding = 'utf-8'
    email.send()
    
    print(f"[DEBUG] Email enviado")
    
    return f"Email enviado con {orders_today.count()} pedidos"