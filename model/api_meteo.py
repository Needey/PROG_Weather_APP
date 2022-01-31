import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')

class api:

    # lieu du temps

    def getLocationData(self, name):
        data = self.weatherData['location'][name] 
        return str(data)
    
    # temp actuel

    def getCurrentData(self, name):
        data = self.weatherData['current'][name]
        return data if name in ('condition','air_quality') else str(data)
    
    
    def fetch(self,query):
            try:
                url = f'http://api.weatherapi.com/v1/current.json' + \
                    f'?key={API_KEY}&q={query}&aqi=yes&lang=fr'
                self.weatherData = requests.get(url).json()
            except:
                self.weatherData = {'error': []}


if __name__ == "__main__":
    pass
