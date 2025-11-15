from django.utils import timezone
from django.core.mail import send_mail
from home.models import Order


def send_daily_order_summary():
    # Fecha actual (dentro de la tarea)
    today = timezone.localdate()
    
    # Pedidos del día
    orders_today = Order.objects.filter(created_at__date=today)
    
    summaries = []
    
    if orders_today.exists():
        for order in orders_today:
            summary = f"{order.get_items_summary()}\nPedido por {order.customer_name} a la dirección {order.delivery_address}"
            summaries.append(summary)
        
        body = "\n\n".join(summaries)
    else:
        body = "Hoy no se han registrado pedidos."
    
    # Enviar email
    send_mail(
        subject=f"Resumen de pedidos del {today}",
        message=body,
        from_email="artemisitcompany@gmail.com",
        recipient_list=["alecarrei1@alum.us.es"],
    )
    
    return f"Email enviado con {orders_today.count()} pedidos"