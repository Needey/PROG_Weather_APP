class TemperatureType:

    def __init__(self : object, current_temp_f : float, current_temp_c : float, feels_like_f : float, feels_like_c : float):

        def check_temp(value):
            if value >= -80 and value <= 80: 
                return True
            else: 
                return False

        if check_temp(current_temp_c) or check_temp(feels_like_c):
            self.current_temp_f = current_temp_f
            self.current_temp_c = current_temp_c
            self.feels_like_f = feels_like_f
            self.feels_like_c = feels_like_c

        else : 
            self.current_temp_f = -999
            self.current_temp_c = -999
            self.feels_like_f = -999
            self.feels_like_c = -999