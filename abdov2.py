class car:
    def __init__(self,speed):
        
        self.__speed = speed
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_all_info(self):
        return [self.__speed]
std1 = car( 20)
print(std1.get_all_info())