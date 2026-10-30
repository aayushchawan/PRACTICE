# Circumference of a circle program

import math


radius = float(input(f"Enter the radius of the circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is {round(circumference, 3)} cm")