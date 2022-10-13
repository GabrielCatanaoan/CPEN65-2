import math


class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter

    def area_radius(self):
        return 'Area of the Circle using radius={}'.format(round((math.pi * self.radius ** 2),3))

    def area_diameter(self):
        return 'Area of the Circle using diameter={}'.format(round((math.pi * (self.diameter/2) ** 2),3))

rad_dia = Circle(float(input('input radius(put zero if none)= ')), float(input('input diameter(put zero if none)= ')))

print(rad_dia.area_radius())
print(rad_dia.area_diameter())
