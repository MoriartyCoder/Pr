class Vehicle:
    def __init__(self, number_of_wheels: int = 4, driven_km: int = 0, fuel_level: int = 0, name: str = str(),
                 capacity: int = 50):
        for atr, val in zip(locals().keys(), locals().values()):
            setattr(self, atr, val)

        self.last_inspection_km = 0

    def drive(self, _km):
        if self.fuel_level - (_km / 10) >= 0:
            self.driven_km += _km
            self.fuel_level -= (_km / 10)
            return

        self.driven_km += self.fuel_level * 10
        self.fuel_level = 0
        raise Exception("no more fuel, hope you're close to some gasoline :(")

    def refuel(self, liters: float = -1):
        if liters == -1 or self.fuel_level + liters > self.capacity:
            self.fuel_level = self.capacity
        elif liters > 0:
            self.fuel_level += liters
        else:
            raise Exception("invalid value for liters")

    def need_inspection(self) -> bool:
        return (self.driven_km - self.last_inspection_km) >= 1000

    def do_inspection(self):
        if self.need_inspection():
            self.last_inspection_km += 1000

    def obd(self):
        for key, value in self.__dict__.items():
            print(f"OBD Vehicle: {key}: {value}")
        print()

    @staticmethod
    def honk():
        print("Tut tut")


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


class Audi(Car):
    def __init__(self, car_name, max_speed):
        super().__init__(car_name, max_speed)

    def obd(self):
        for key, value in self.__dict__.items():
            print(f"OBD Audi: {key}: {value}")
        print()


class BMW(Car):
    def __init__(self, car_name, max_speed):
        super().__init__(car_name, max_speed)

    def obd(self):
        for key, value in self.__dict__.items():
            print(f"OBD BMW: {key}: {value}")
        print()

    def online_inspection(self):
        self.do_inspection()


class Truck(Vehicle):

    def __init__(self, car_name):
        super().__init__(name=car_name, number_of_wheels=10)

        self.current_load = []
        self.max_load = 20

    def load(self, new_load):
        for l in new_load:
            if len(self.current_load) > self.max_load:
                break

            self.current_load.append(l)

    def unload(self, unload_packages):
        for i in range(unload_packages):
            if len(self.current_load):
                self.current_load.pop()
            else:
                break


class Pickup(Car, Truck):

    def __init__(self, car_name, max_speed, max_passangers):
        Car.__init__(self, car_name, max_speed, max_passangers)
        Truck.__init__(self, car_name)

    def obd(self):
        super(Car, self).obd()
        super(Truck, self).obd()
        print()


if __name__ == '__main__':
    audi_car = Audi("A6", 320)
    audi_car.obd()

    bmw_car = BMW("M6", 340)
    bmw_car.refuel(100)
    bmw_car.drive(200)
    bmw_car.obd()
    bmw_car.get_in(5)
    bmw_car.online_inspection()
    bmw_car.obd()

    man = Truck("MAN")
    man.obd()
    man.load([10, 24, 5, 34])
    man.obd()
    man.unload(2)
    man.obd()
    man.load([10, 24, 5, 34, 80])
    man.obd()
    man.unload(10)
    man.obd()

    ford = Pickup("F-150", 180, 25)
    ford.refuel(130)
    ford.get_in(3)
    ford.drive(100)
    ford.load([2, 5, 11])
    ford.obd()
