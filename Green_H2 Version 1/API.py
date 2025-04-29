import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import time
import re

address = "Mansoura - Egypt"
geolocater = Nominatim(user_agent="geoapiExercise")
location = geolocater.geocode(address)

obj = TimezoneFinder()
result = obj.timezone_at(lng = location.longitude,lat = location.latitude )

lat = str(location.latitude)
lon = str(location.longitude)
# print(lat)
# print(lon)


def weather ():
    api = "https://api.openweathermap.org/data/2.5/weather?lat=31.037933&lon=31.381523&appid=846eb25def35d0c7ec3284d8e8932314"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    Max_temp = int(json_data['main']['temp_max'] - 273.15)
    preseure = json_data['main']['pressure']
    hunuidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S %p",time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S  %p",time.gmtime(json_data['sys']['sunset']))
    
    temp1 = json_data['daily']
    
    final_info = condition + "\n" + str(temp) + '\n' + str(Max_temp) +"\n" +str(sunrise) + "\n" + str(sunset)
    print(final_info)

def future():
    api2 = "https://api.open-meteo.com/v1/forecast?latitude=31.037933&longitude=31.381523&current=relative_humidity_2m,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,wind_speed_10m_max&timezone=Africa%2FCairo&past_days=1&forecast_days=16"
    json_data = requests.get(api2).json()
    current = json_data["daily"]['temperature_2m_max'][0]
    tempday1 = json_data['daily']['temperature_2m_max'][1]
    tempday2 = json_data['daily']['temperature_2m_max'][2]
    tempday3 = json_data['daily']['temperature_2m_max'][3]
    tempday4 = json_data['daily']['temperature_2m_max'][4]
    tempday5 = json_data['daily']['temperature_2m_max'][5]
    tempday6 = json_data['daily']['temperature_2m_max'][6]
    tempday7 = json_data['daily']['temperature_2m_max'][7]
    
    current_min = json_data["daily"]['temperature_2m_min'][0]
    tempday1_min = json_data['daily']['temperature_2m_min'][1]
    tempday2_min = json_data['daily']['temperature_2m_min'][2]
    tempday3_min = json_data['daily']['temperature_2m_min'][3]
    tempday4_min = json_data['daily']['temperature_2m_min'][4]
    tempday5_min = json_data['daily']['temperature_2m_min'][5]
    tempday6_min = json_data['daily']['temperature_2m_min'][6]
    tempday7_min = json_data['daily']['temperature_2m_min'][7]
    
    current_speed = json_data["daily"]["wind_speed_10m_max"][0]
    tempday1_speed = json_data['daily']["wind_speed_10m_max"][1]
    tempday2_speed = json_data['daily']["wind_speed_10m_max"][2]
    tempday3_speed = json_data['daily']["wind_speed_10m_max"][3]
    tempday4_speed = json_data['daily']["wind_speed_10m_max"][4]
    tempday5_speed = json_data['daily']["wind_speed_10m_max"][5]
    tempday6_speed = json_data['daily']["wind_speed_10m_max"][6]
    tempday7_speed = json_data['daily']["wind_speed_10m_max"][7]
    
    sunset = json_data["daily"]["sunset"][0]
    result1 = re.findall(r"[0-9]+:[0-9]+",sunset)
    sunset_1 = result1[0]
    
    sunrise = json_data["daily"]["sunrise"][0]
    result1 = re.findall(r"[0-9]+:[0-9]+",sunrise)
    sunrise_1 = result1[0]
    
    print(sunrise_1)
    
    
    

future()

