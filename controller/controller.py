
from model.api_meteo import api
from model.weather import Weather
from view.view import View

class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()
        self.api = api()

        self.update()


    def main(self):
        self.view.main()

    
    def update(self):
        if 'error' not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.getLocation().city)
            self.view.varCondition.set(self.weather.getWeather().weather_condition)
            self.view.varWindSpeed.set(self.weather.getWind().wind_speed_mph)
            self.view.varWindDir.set(self.weather.getWind().wind_direction)
            self.view.varIcon.set(self.weather.getWeather().weather_icon_path)

            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.getTemperature().current_temp_f)
                self.view.varFeelsLike.set(self.weather.getTemperature().feels_like_f)
            else:
                self.view.varTemp.set(self.weather.getTemperature().current_temp_c)
                self.view.varFeelsLike.set(self.weather.getTemperature().feels_like_c)


    def handleButtonSearch(self, event=None):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.update()
