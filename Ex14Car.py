from Ex14Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, car_name, max_speed, max_passangers: int = 5):
        Vehicle.__init__(self, name=car_name)
        self.cnt_passangers = 0
        self.max_passangers = max_passangers
        self.max_speed = max_speed

    def get_out(self, sub):
        self.cnt_passangers = max(0,
                                  self.cnt_passangers - sub)

    def get_in(self, add):
        self.cnt_passangers = min(self.max_passangers,
                                  self.cnt_passangers + add)

    def get_passangers(self):
        return self.cnt_passangers

    def get_max_passangers(self):
        return self.max_passangers
