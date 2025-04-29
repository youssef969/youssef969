import requests
import datetime
import re
class Data:
    def __init__(self):
        api2 = "https://api.open-meteo.com/v1/forecast?latitude=31.037933&longitude=31.381523&current=wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,wind_speed_10m_max&timezone=Africa%2FCairo&forecast_days=14"
        json_data = requests.get(api2).json()
        self.current = json_data["daily"]['temperature_2m_max'][0]
        self.day1_temp = json_data['daily']['temperature_2m_max'][1]
        self.day2_temp = json_data['daily']['temperature_2m_max'][2]
        self.day3_temp = json_data['daily']['temperature_2m_max'][3]
        self.day4_temp = json_data['daily']['temperature_2m_max'][4]
        self.day5_temp = json_data['daily']['temperature_2m_max'][5]
       
        self.current_sunrise = json_data["daily"]["sunrise"][0]
        self.day1_sunrise = json_data['daily']['sunrise'][1]
        self.day2_sunrise = json_data['daily']['sunrise'][2]
        self.day3_sunrise = json_data['daily']['sunrise'][3]
        self.day4_sunrise = json_data['daily']["sunrise"][4]
        self.day5_sunrise = json_data['daily']['sunrise'][5]
        
        self.current_sunset = json_data["daily"]["sunset"][0]
        self.day1_sunset = json_data['daily']['sunset'][1]        
        self.day2_sunset = json_data['daily']['sunset'][2]
        self.day3_sunset = json_data['daily']['sunset'][3]
        self.day4_sunset = json_data['daily']["sunset"][4]
        self.day5_sunset = json_data['daily']['sunset'][5]
        
        self.current_speed = json_data["daily"]["wind_speed_10m_max"][0]
        self.day1_speed = json_data['daily']["wind_speed_10m_max"][1]
        self.day2_speed = json_data['daily']["wind_speed_10m_max"][2]
        self.day3_speed = json_data['daily']["wind_speed_10m_max"][3]
        self.day4_speed = json_data['daily']["wind_speed_10m_max"][4]
        self.day5_speed = json_data['daily']["wind_speed_10m_max"][5]
        
        self.sunrise_1=self.Sunset(self.current_sunrise,self.current_sunset)[0]
        self.sunrise_2=self.Sunset(self.day1_sunrise,self.day1_sunset)[0]
        self.sunrise_3=self.Sunset(self.day2_sunrise,self.day2_sunset)[0]
        self.sunrise_4=self.Sunset(self.day3_sunrise,self.day3_sunset)[0]
        self.sunrise_5=self.Sunset(self.day4_sunrise,self.day4_sunset)[0]
        self.sunrise_6=self.Sunset(self.day5_sunrise,self.day5_sunset)[0]
        
        self.sunset_1=self.Sunset(self.current_sunrise,self.current_sunset)[1]
        self.sunset_2=self.Sunset(self.day1_sunrise,self.day1_sunset)[1]
        self.sunset_3=self.Sunset(self.day2_sunrise,self.day2_sunset)[1]
        self.sunset_4=self.Sunset(self.day3_sunrise,self.day3_sunset)[1]
        self.sunset_5=self.Sunset(self.day4_sunrise,self.day4_sunset)[1]
        self.sunset_6=self.Sunset(self.day5_sunrise,self.day5_sunset)[1]
        
        self.power_1 = self.Solar_Panel_Elec(self.sunrise_1,self.sunset_1,self.current)
        self.power_2 = self.Solar_Panel_Elec(self.sunrise_2,self.sunset_2,self.day1_temp)
        self.power_3 = self.Solar_Panel_Elec(self.sunrise_3,self.sunset_3,self.day2_temp)
        self.power_4 = self.Solar_Panel_Elec(self.sunrise_4,self.sunset_4,self.day3_temp)
        self.power_5 = self.Solar_Panel_Elec(self.sunrise_5,self.sunset_5,self.day4_temp)
        self.power_6 = self.Solar_Panel_Elec(self.sunrise_6,self.sunset_6,self.day5_temp)

    def Solar_Panel_Elec(self,sunrise,sunset,temperature):
        self.sunset_var = datetime.datetime.strptime(sunset,"%H:%M").time()    # time format
        self.sunrise_var = datetime.datetime.strptime(sunrise,"%I:%M").time()   # time format
        time1 = datetime.timedelta(hours=self.sunrise_var.hour,minutes=self.sunrise_var.minute)
        time2 = datetime.timedelta(hours=self.sunset_var.hour,minutes=self.sunset_var.minute)
        duration = time2-time1
        hours = duration.total_seconds()/3600.0 
            
        if temperature <= 24:
            elec = hours * 10.0   
        elif temperature > 24 :
            diff = temperature - 24   # subtract current temp from 24
            amount_of_inefficiency = 1 - (diff * 0.004) # multiply diff in amount of inefficiency and subtract from 1 to have the final result 
            elec = 10.0 * hours * amount_of_inefficiency
        return elec
    
    def Sunset(self,sunrise,sunset):
        result1 = re.findall(r"[0-9]+:[0-9]+",sunset)
        sunset_1 = result1[0]
        
        result2 = re.findall(r"[0-9]+:[0-9]+",sunrise)
        sunrise_1 = result2[0]
        return sunrise_1 ,sunset_1