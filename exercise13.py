from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, number_of_wheels: int = 4, driven_km: int = 0, fuel_level: int = 0, name: str = str(),
                 capacity: int = 50):
        self.number_of_wheels = number_of_wheels
        self.__km = driven_km
        self.__fuel = fuel_level
        self.name = name
        self.capacity = capacity

        self.__last_inspection = 0


    """
    Returns number of wheels.
    """
    def get_nr_wheels(self):
        return self.number_of_wheels

    """
    Sets number of wheels.
    
    new_number_of_wheels: New number of wheels.
    """
    def set_nr_wheels(self, new_number_of_wheels):
        self.number_of_wheels = new_number_of_wheels


    """
    \"Drives\" the car for a certain distance [km]. If it drives longer than there is fuel for, the car stops.
    
    _km: Km that the car drives.
    """
    def drive(self, _km):
        if self.__fuel - (_km / 10) >= 0:
            self.__km += _km
            self.__fuel -= (_km / 10)
        else:
            self.__km += self.__fuel * 10
            self.__fuel = 0
            raise Exception("no more fuel, hope you're close to some gasoline :(")

    """
    Refules the car.
    
    liters (float = -1): The amount of liters shall be refueled. 
                         If the value is -1 or the actual capacity 
                         plus the added liters are more than the 
                         maximum capacity than the new is set to the 
                         maximum capacity.
    """
    def refuel(self, liters: float = -1):
        if liters == -1 or self.__fuel + liters > self.capacity:
            self.__fuel = self.capacity
        elif liters > 0:
            self.__fuel += liters
        else:
            raise Exception("invalid value for liters")

    """
    Returns the boolean value whether the car needs an inspection or not.
    """
    def need_inspection(self) -> bool:
        return (self.__km - self.__last_inspection) >= 1000

    """
    Does the inspection of the car.
    """
    def do_inspection(self):
        if self.need_inspection():
            self.__last_inspection += 1000

    """
    Shows the attributes and its values of the instance.
    
    with_print: When true the string gets also printed.
    """
    def obd(self, with_print=False):
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key}: {value}\n"

        if with_print:
            print(result + "\n")

        return result

    def __str__(self):
        return self.obd()

    def __add__(self, other):
        print(f"A car accident happend:\nA {self.name} and a {other.name} crashed.\n{self.get_nr_wheels() + other.get_nr_wheels()} flew around.")

    """
    Static method that checks weather the car is already an oldtimer or not.
    To be an oldtimer it needs to be older than 30 years.
    """
    @staticmethod
    def is_oldtimer(year_to_check: int):
        return 2020 - year_to_check > 30

    """
    Abstract method for the sound of the horn of the Vehicle
    """
    @abstractmethod
    def honk(self):
        pass

class Car(Vehicle):
    """
    car_name: Name of the car.
    max_speed (int): Maximum speed the car can drive.
    max_passangers (int): Maximus of passangers the car can hold. Default value is 5.
    """
    def __init__(self, car_name, max_speed: int, max_passangers: int = 5):
        Vehicle.__init__(self, name=car_name)
        self.cnt_passangers = 0
        self.max_passangers = max_passangers
        self.max_speed = max_speed

    """
    sub: Number of passangers that shall be subtracted from the counter of passangers
    
    Note: It is not possible to have less than 0 passangers!
    """
    def get_out(self, sub):
        self.cnt_passangers = max(0,
                                  self.cnt_passangers - sub)

    """
    add: Add this number of passangers to the current number of passangers
    
    This function adds passangers to the counter. But the new number can not execced the maximum.
    """
    def get_in(self, add):
        self.cnt_passangers = min(self.max_passangers,
                                  self.cnt_passangers + add)

    """
    Returns the number of passangers in the car.
    """
    def get_passangers(self):
        return self.cnt_passangers

    """
    Returns the max number of passangers that are allowed in the car.
    """
    def get_max_passangers(self):
        return self.max_passangers

    """
    This method prints the sound of the horn of the car.
    Due to the inheritance from Vehicle and that it is there
    a abstract method, it needed to be implemented here.
    """
    def honk(self):
        print("TUT TUT")

if __name__ == '__main__':
    """
    a = Vehicle(name="Audi")
    print(a)
    b = Vehicle(name="BMW")

    a + b
    """

    a = Car("Audi", 320)
    a.honk()

    print(Vehicle.is_oldtimer(2000))
    print(Vehicle.is_oldtimer(1800))
    pass
