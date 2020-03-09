# define vehicle class here

class Vehicle:

# characteristics
    def __init__(self, size_cargo, chasis, wheels, n_passengers):
        self.engine = size_cargo
        self.chasis = chasis
        self.wheels = wheels
        self.n_passengers = n_passengers
    # n_passengers
    # size cargo
    def acceleration(self):
        return 'VVVRUMM'
    def brakes(self):
        return 'eeeeeek'
    # methods :
# acceleration
# brakes