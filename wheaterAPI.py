import os
import json
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
class WeatherAPI:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.datos = []

    def build_url(self):
        return f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={self.city}&days=1&aqi=no&alerts=no"

    def get_forecast(self, response, i):  # Agregar 'self'
        date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
        hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
        condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
        temp = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
        rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
        rain_prob = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
        return date, hour, condition, temp, rain, rain_prob
    
    def request_weather(self):
        try:
            response = requests.get(self.build_url()).json()
            for i in range(len(response['forecast']['forecastday'][0]['hour'])):
                self.datos.append(self.get_forecast(response, i))  # Agregar 'self.'
            return self.dataframe_build()
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return {"error": str(e)}
        
        
    def dataframe_build(self):
        col = ['Data', 'Hour', 'Condition', 'Temperature', 'Rain', 'Rain_prob']
        df = pd.DataFrame(self.datos, columns=col)
        df_rain = df[(df['Rain'] == 1) & (df['Hour'] > 6) & (df['Hour'] < 22)]
        df_rain = df_rain[['Hour', 'Condition']]
        df_rain.set_index('Hour', inplace= True)
        df_rain.reset_index(inplace=True)
        return df_rain

