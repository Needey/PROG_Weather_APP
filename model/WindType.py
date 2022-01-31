class WindType:
    
    def __init__(self : object, wind_speed_mph : float, wind_speed_kph : float, wind_degree : int, wind_direction : str, gust_speed_mph : float, gust_speed_kph : float):
        
        def check_wind_speed(value):
            if value >= 0 and value <= 231:
                return True
            else:
                return False

        def check_wind_degree(value):
            if value <= 360 and value >= 0:
                return True
            else:
                return False

        self.wind_speed_mph = wind_speed_mph if check_wind_speed(wind_speed_kph) else -1
        self.wind_speed_kph = wind_speed_kph if check_wind_speed(wind_speed_kph) else -1
        self.wind_degree = wind_degree if check_wind_degree(wind_degree) else -1
        self.wind_direction = wind_direction
        self.gust_speed_mph = gust_speed_mph
        self.gust_speed_kph = gust_speed_kph