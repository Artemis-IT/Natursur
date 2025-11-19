# Configuración de Twilio (Envío de SMS)

## Descripción

El proyecto utiliza Twilio para enviar notificaciones SMS a los clientes cuando realizan un pedido. El SMS incluye el precio total del pedido, instrucciones de pago vía Bizum y el número de referencia del pedido.

## Requisitos Previos

1. Crear una cuenta en [Twilio](https://www.twilio.com/)
2. Verificar un número de teléfono de prueba (en cuenta gratuita)
3. Obtener las credenciales de la cuenta

## Variables de Entorno Necesarias

Añadir las siguientes variables al archivo `.env`:

```env
TWILIO_ACCOUNT_SID=tu_account_sid_aqui
TWILIO_AUTH_TOKEN=tu_auth_token_aqui
TWILIO_PHONE_NUMBER=+34XXXXXXXXX
```

### Obtener las Credenciales

1. **Account SID y Auth Token:**
   - Acceder al [Dashboard de Twilio](https://console.twilio.com/)
   - Copiar el "Account SID" y "Auth Token" de la sección "Account Info"

2. **Número de Teléfono:**
   - En el Dashboard, ir a "Phone Numbers" → "Manage" → "Active Numbers"
   - Copiar el número de teléfono proporcionado por Twilio
   - Formato: `+34XXXXXXXXX` (incluir el código de país)

## Funcionalidad

### Envío Automático de SMS

Cuando un cliente completa un pedido, el sistema envía automáticamente un SMS con:

- **Total del pedido** en euros
- **Número de Bizum** para realizar el pago
- **Referencia del pedido** para seguimiento

**Ejemplo de SMS:**
```
Natursur - Realice el pago
Total: 45.99€
Bizum: 600000000
Ref: PEDIDO#123
```

### Implementación en el Código

El archivo `tienda_virtual/home/send_sms.py` contiene la función principal:

```python
def send_price_sms(order, price):
    """Envía SMS con el precio del pedido al cliente."""
    # Se ejecuta automáticamente al confirmar un pedido
```

## Limitaciones de la Cuenta Gratuita

- **Saldo limitado:** Twilio ofrece crédito gratuito limitado
- **Números verificados:** Solo se pueden enviar SMS a números previamente verificados
- **Marca de prueba:** Los mensajes incluyen un prefijo de "Sent from your Twilio trial account"

## Para Producción

1. Actualizar a una cuenta de pago en Twilio
2. Comprar un número de teléfono dedicado
3. Verificar el dominio del negocio
4. Configurar las variables de entorno en el servidor de producción (Render)

## Resolución de Problemas

### Error: "The number is unverified"
- **Solución:** Verificar el número del cliente en el panel de Twilio (Phone Numbers → Verified Caller IDs)

### Error: "Insufficient funds"
- **Solución:** Añadir crédito a la cuenta de Twilio

### No se envía el SMS
1. Verificar que las credenciales en `.env` sean correctas
2. Comprobar que el número de teléfono incluya el código de país
3. Revisar los logs de Django para ver errores específicos

## Referencias

- [Documentación oficial de Twilio](https://www.twilio.com/docs)
- [Twilio Python SDK](https://www.twilio.com/docs/libraries/python)
- [Consola de Twilio](https://console.twilio.com/)
