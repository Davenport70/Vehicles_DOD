from vehicle_class import *

class plane:
# characteristics
    def __init__(self, brand, n_passengers, size_cargo):
        self.brand = brand
        self.n_passengers = n_passengers
        self.size_cargo = size_cargo

    def take_off(self):
        return 'Weeeeooooo'
    def land(self):
        return 'OOOOOweeee'