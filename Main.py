import sys 
sys.path.append("C:\\PythonLibs")
import twilio
import os 
from twilio.rest import Client
import time
import pandas as pd
import requests
from sendMessageTwilio import TwilioMessenger
from wheaterAPI import WeatherAPI
from dotenv import load_dotenv 

load_dotenv("credenciales.env")


weather_api = WeatherAPI("Buenos Aires", "f1a8617a43e948a6a55150725250602")
rain_hours = weather_api.request_weather()
def message_definition(rain_hours):
    if rain_hours.empty: 
        return "no va a llover"
    else:
        conditions_and_hours = '\n'.join(f"Hora: {row['Hour']}, Condición: {row['Condition']}" for index, row in rain_hours.iterrows())
        return  "Buen dia, Joaco hoy va a llover,\n" + conditions_and_hours
# Crear instancia de TwilioMessenger
# Configuración de credenciales de Twilio
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
# Enviar el mensaje con un nombre dinámico
message = message_definition(rain_hours)

to_number = "+541164821004"

messenger = TwilioMessenger(ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER)

message_sid = messenger.send_message(message, to_number)

