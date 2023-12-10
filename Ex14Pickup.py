from Ex14Truck import Truck
from Ex14Car import Car

class Pickup(Car, Truck):

    def __init__(self, car_name, max_speed, max_passangers):
        Car.__init__(self, car_name, max_speed, max_passangers)
        Truck.__init__(self, car_name)

    def obd(self):
        super(Car, self).obd()
        super(Truck, self).obd()
        print()