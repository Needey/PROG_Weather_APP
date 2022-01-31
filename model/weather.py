from model.LocationType import LocationType
from model.TemperatureType import TemperatureType
from model.WindType import WindType
from model.AirType import AirType
from model.WeatherType import WeatherType
from model.api_meteo import api

class Weather:
    api=api()
    def __init__(self, location:str='Paris'):
        self.weatherData = {}
        self.api.fetch(location)

    #---- Location ----- #

    def getLocation(self):
        city = str(self.api.getLocationData('name')) # Location name
        state = str(self.api.getLocationData('region')) # Region or state of the location, if availa
        country = str(self.api.getLocationData('country')) # Location country
        time_zone = str(self.api.getLocationData('tz_id')) # Time zone name
        lat = float(self.api.getLocationData('lat')) # Latitude in decimal degree
        lon = float(self.api.getLocationData('lon')) # Longitude in decimal degree
        localtime_epoch = int(self.api.getLocationData('localtime_epoch')) # Local date and time in unix time
        localtime = str(self.api.getLocationData('localtime')) # Local date and time
        
        Location = LocationType(city, state, country, time_zone, lat, lon, localtime_epoch, localtime)
        return Location


    #---- Temperature ----- #
    
    def getTemperature(self):
        current_temp_f = float(self.api.getCurrentData('temp_f')) # Temperature in fahrenheit
        current_temp_c = float(self.api.getCurrentData('temp_c')) # Temperature in celsius
        feels_like_f = float(self.api.getCurrentData('feelslike_f')) # Feels like temperature as fahrenheit
        feels_like_c = float(self.api.getCurrentData('feelslike_c')) # Feels like temperature as celcius
        
        Temperature = TemperatureType(current_temp_f, current_temp_c, feels_like_f, feels_like_c)
        return Temperature
    
    
    #---- Wind ----- #
    
    def getWind(self):
        wind_speed_mph = float(self.api.getCurrentData('wind_mph')) # Maximum wind speed in miles per hour
        wind_speed_kph = float(self.api.getCurrentData('wind_kph')) # Maximum wind speed in kilometer per hour
        wind_degree = int(self.api.getCurrentData('wind_degree')) # Wind direction in degrees
        wind_direction = str(self.api.getCurrentData('wind_dir')) # Wind direction as 16 point compass. e.g.: NSW
        gust_speed_mph = float(self.api.getCurrentData('gust_mph')) # Wind gust in miles per hour
        gust_speed_kph = float(self.api.getCurrentData('gust_kph')) # Wind gust in kilometer per hour
        
        Wind = WindType(wind_speed_mph, wind_speed_kph, wind_degree, wind_direction, gust_speed_mph, gust_speed_kph)
        return Wind
    
    
    #---- Air ----- #
    
    def getAir(self):
        pressure_mb = float(self.api.getCurrentData('pressure_mb')) # Pressure in millibars
        pressure_in = float(self.api.getCurrentData('pressure_in')) # Pressure in inches
        humidity = int(self.api.getCurrentData('humidity')) # Humidity as percentage
        co = float(self.api.getCurrentData('air_quality')['co']) # 	Carbon Monoxidg/m3)
        no2 = float(self.api.getCurrentData('air_quality')['no2']) # Nitrogen dioxide (μg/m3)
        o3 = float(self.api.getCurrentData('air_quality')['o3']) # 	NOzone (μg/m3)
        so2 = float(self.api.getCurrentData('air_quality')['so2']) # Sulphur dioxide (μg/m3)
        pm2_5 = float(self.api.getCurrentData('air_quality')['pm2_5']) # PM2.5 (μg/m3)
        pm10 = float(self.api.getCurrentData('air_quality')['pm10']) # PM10 (μg/m3)
        us_epa_index = int(self.api.getCurrentData('air_quality')['us-epa-index']) # US - EPA standard
        gb_defra_index = int(self.api.getCurrentData('air_quality')['gb-defra-index']) # UK Defra Index
        
        Air = AirType(pressure_mb, pressure_in, humidity, co, no2, o3, so2, pm2_5, pm10, us_epa_index, gb_defra_index)
        return Air
    
    
    #---- Weather ----- #
    
    def getWeather(self):
        weather_condition = str(self.api.getCurrentData('condition')['text']) # Weather condition text
        weather_icon_path = 'http:'+str(self.api.getCurrentData('condition')['icon']) # Weather icon url
        precip_mm = float(self.api.getCurrentData('precip_mm')) # Precipitation amount in millimeters
        precip_in = float(self.api.getCurrentData('precip_in')) # Precipitation amount in inches
        cloud = int(self.api.getCurrentData('cloud')) # Cloud cover as percentage
        is_day = int(self.api.getCurrentData('is_day')) # Whether to show day condition icon or night icon
        uv_index = float(self.api.getCurrentData('uv')) # UV Index
        avgvis_km = float(self.api.getCurrentData('vis_km')) # Average visibility in kilometer
        avgvis_miles = float(self.api.getCurrentData('vis_miles')) # Average visibility in miles
        
        Weather = WeatherType(weather_condition, weather_icon_path, precip_mm, precip_in, cloud, is_day, uv_index, avgvis_km, avgvis_miles)
        return Weather

