from django.conf import settings
from twilio.rest import Client


def send_price_sms(order, price):
    """Envía SMS con el precio del pedido al cliente."""
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        message_body = f"""Natursur - Realice el pago
        Total: {price}€
        Bizum: 600000000
        Ref: PEDIDO#{order.id}"""
        
        # Enviar SMS
        message = client.messages.create(
            body=message_body,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=order.customer_phone
        )
        
        print(f"SMS enviado. SID: {message.sid}")
        return True
        
    except Exception as e:
        print(f"Error enviando SMS: {e}")
        return False