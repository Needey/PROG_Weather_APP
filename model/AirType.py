class AirType:
    
    def __init__(self : object, pressure_mb : float, pressure_in : float, humidity : int, co : float, no2 : float, o3 : float, so2 : float, pm2_5 : float, pm10 : float, us_epa_index : int, gb_defra_index : int):

        def check_humidity(value):
            if value >= 0 and value <= 100 : 
                return True
            else :
                return False
                
        self.pressure_mb = pressure_mb
        self.pressure_in = pressure_in
        self.lat = humidity if check_humidity(humidity) else -1
        self.co = co
        self.no2 = no2
        self.o3 = o3
        self.so2 = so2
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.us_epa_index = us_epa_index
        self.gb_defra_index = gb_defra_index