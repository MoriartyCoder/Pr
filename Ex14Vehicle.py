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
