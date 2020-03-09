# important all the classes
from vehicle_class import *
from car_class import *
from plane_class import *

# create 2 vehicles
my_car = car('volvo S60', 400, 220, 5)
daves_car = car('fiat 500', 200, 110, 3)
# call methods and attributes to test
# create 2 cars instances
print(type(my_car))
print(daves_car)
print(my_car.brand)
print(my_car.horsepower)
print(daves_car.n_doors)
# make car accelerate and make them brake
# make car honk and park
print(my_car.honk())
print(daves_car.park())
# create 2 planes instances here
plane1 = plane('emirates', 500, 1000)
# make plane accelerate and make them brake
print(plane1.acceleration())
print(plane1.brakes())
print(plane1.take_off())
print(plane1.brakes())
# make plane fly and land