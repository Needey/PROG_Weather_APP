
class WeatherType:
    
    def __init__(self : object, weather_condition : str, weather_icon_path : str, precip_mm : float, precip_in : float, cloud : int, is_day : int, uv_index : float, avgvis_km : float, avgvis_miles : float):
        
        def check_uv_index(value):
            if value >= 0 and value <= 10: 
                return True
            else: 
                return False
            
        def check_cloud(value):
            if value >= 0 and value <= 100: 
                return True
            else: 
                return False
        
        self.weather_condition = weather_condition
        self.weather_icon_path = weather_icon_path
        self.precip_mm = precip_mm
        self.precip_in = precip_in
        self.cloud = cloud if check_cloud(cloud) else -1
        self.is_day = is_day
        self.uv_index = uv_index if check_uv_index(uv_index) else -1
        self.avgvis_km = avgvis_km
        self.avgvis_miles = avgvis_miles
        
        
        
        