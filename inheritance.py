class Vehicle:  #base class
    def general_usage(self):  #method
        print("general use: transportation")

class Car(Vehicle): #subclass, inherits from Vehicle class(base class)
    def __int__(self):
        print("I'm car")
        self.wheels = 4 #Properties
        self.has_roof = True  #Properties
    def specific_usage(self):
        print("specif use: commute to work, vacation with family")

class Motocycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2 # Properties
        self.has_roof = False  # Properties
    def specific_usage(self):
        print("specif use: croad trip, racing")

c = Car()
c.general_usage()
c.specific_usage()

m = Motocycle()
m.general_usage()
m.specific_usage()

        