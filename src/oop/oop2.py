# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

# Comeback to this


class GroundVehicle():
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        if None == num_wheels:
            print(4)
        else:
            print(num_wheels)

    def drive(self):
        print("vrooom")

    # TODO


weird_car = GroundVehicle(5).drive()


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels):
        super().__init__(num_wheels)

    def drive(self):
        print("BRAAAP!!")


motorcycle = Motorcycle(2).drive()


# TODO


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
# TODO
