# ⛈ Notificaciones de Lluvia con Python, Pandas, Twilio y AWS EC2 ⛈

## 💻 Descripción
Este proyecto es un bot automatizado que envía un mensaje SMS diario notificando si va a llover durante el día. Para lograrlo, el script obtiene el pronóstico del clima desde la API de **WeatherAPI**, procesa los datos con **Pandas** y usa **Twilio** para enviar el mensaje.

El bot está desplegado en una instancia **AWS EC2** y programado con **cronjob** para ejecutarse diariamente.

## 🌐 Tecnologías Utilizadas
- **Python** – Para la lógica del script.
- **Pandas** – Para transformar y analizar el JSON del pronóstico del clima.
- **Twilio API** – Para enviar SMS con la notificación del clima.
- **WeatherAPI** – Para obtener el pronóstico meteorológico.
- **AWS EC2** – Para alojar y ejecutar el script.
- **Cronjob** – Para programar la ejecución diaria del bot.
- **dotenv** – Para manejar credenciales de manera segura.

## ⚙️ Instalación y Configuración
