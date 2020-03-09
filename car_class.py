# important my vehicle class
from vehicle_class import *

# design car class here and make it inherit vehicle
class Car(Vehicle):
# characteristics
    def __init__(self, brand, horsepower, max_speed, n_doors):
        self.brand = brand
        self.horsepower = horsepower
        self.max_speed = max_speed
        self.n_doors = n_doors
    # brand
    # horsepower
    # make speed
    def park(self):
        return 'parking'
    def honk(self):
        return 'beep beep'
# methods
# park
# honk