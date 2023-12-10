from Ex14Vehicle import Vehicle

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