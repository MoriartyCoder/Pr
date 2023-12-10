from Ex14Car import Car

class BMW(Car):
    def __init__(self, car_name, max_speed):
        super().__init__(car_name, max_speed)

    def obd(self):
        for key, value in self.__dict__.items():
            print(f"OBD BMW: {key}: {value}")
        print()

    def online_inspection(self):
        self.do_inspection()