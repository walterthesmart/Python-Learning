class Circle:
    import math
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * Circle.pi * self.radius
    
    def area(self):
        return self.pi * self.radius**2

bigCircle = Circle(8)
print(bigCircle.circumference())

Area = Circle(10)
print(Area.area())

        