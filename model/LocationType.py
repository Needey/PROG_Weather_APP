
class LocationType:
    
    def __init__(self : object, city : str, state : str, country : str, time_zone : str, lat : float, lon : float, localtime_epoch : int, localtime : str):
        
        def check_lat(value):
            if value >= -90 and value <= 90:
                return True
            else:
                return False

        def check_lon(value):
            if value >= -180 and value <= 80:
                return True
            else:
                return False
            
        self.city = city
        self.state = state
        self.country = country
        self.time_zone = time_zone
        self.lat = lat if check_lon(lat) else -1
        self.lon = lon if check_lon(lon) else -1
        self.localtime_epoch = localtime_epoch
        self.localtime = localtime