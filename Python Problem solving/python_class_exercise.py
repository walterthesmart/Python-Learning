class Circle:
    import math
    pi = math.pi
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * self.pi * self.radius
    


bigCircle = Circle(4)
print(bigCircle.circumference())
        

        