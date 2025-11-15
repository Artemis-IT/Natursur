from django.utils import timezone
from django.core.mail import EmailMessage
from home.models import Order


def send_daily_order_summary():
    today = timezone.localdate()
    
    orders_today = Order.objects.filter(created_at__date=today)
    
    summaries = []
    
    if orders_today.exists():
        for order in orders_today:
            summary = f"{order.get_items_summary()}\nPedido por {order.customer_name} a la direccion {order.delivery_address}"
            summaries.append(summary)
        
        body = "\n\n".join(summaries)
    else:
        body = "Hoy no se han registrado pedidos."
    
    # Usar EmailMessage en lugar de send_mail para manejar mejor el encoding
    email = EmailMessage(
        subject=f"Resumen de pedidos del {today}",
        body=body,
        from_email="artemisitcompany@gmail.com",
        to=["alecarrei1@alum.us.es"],  # ← Cambia por tu email
    )
    email.content_subtype = "plain"
    email.encoding = 'utf-8'
    email.send()
    
    return f"Email enviado con {orders_today.count()} pedidos"