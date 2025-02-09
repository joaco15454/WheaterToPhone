from twilio.rest import Client
from datetime import datetime

class TwilioMessenger:
    def __init__(self, account_sid, auth_token, from_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number  # Número de origen fijo

    def generate_message(self, message):
        fecha = datetime.now().date()
        return f"Hola Joaco! Hoy {fecha}: {message}."

    def send_message(self, message, to_number):
        """
        Envía un mensaje dinámico basado en el nombre del usuario.
        """
        body = self.generate_message(message)  # Genera el mensaje dinámico
        message = self.client.messages.create(
            body=body,
            from_=self.from_number,
            to=to_number
        )
        return message.sid  # Devuelve el SID del mensaje enviado
