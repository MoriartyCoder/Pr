
from Ex14Pickup import Pickup
from Ex14Car import Car
from Ex14Bmw import BMW
from Ex14Pickup import Pickup
from Ex14Vehicle import Vehicle
from Ex14Truck import Truck
from Ex14Audi import Audi

class Autobahn:

    def __init__(self):
        pass

    @staticmethod
    def start():
        audi_car = Audi("A6", 320)
        audi_car.refuel(100)
        audi_car.drive(200)
        audi_car.obd()

        bmw_car = BMW("M6", 340)
        bmw_car.refuel(100)
        bmw_car.drive(200)

        man = Truck("MAN")
        man.load([10, 24, 5, 34])

        ford = Pickup("F-150", 180, 25)
        ford.refuel(130)
        ford.drive(100)
        ford.load([2, 5, 11])

        car = Car("Lightning MacQueen", 400, 0)
        car.get_in(1)

        vehicle = Vehicle()
        vehicle.honk()

        pass


if __name__ == "__main__": # Cool. Didn't know that!
    print("Start Autobahn-Script")

    Autobahn.start()
