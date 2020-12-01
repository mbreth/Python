# this is a program I wrote to help my niece work on different geometric shapes for her elementary math class.
# this helps find the circumference and diameter of a circle; areas of a triangle and rectangles. Just to make life easier
# --STILL A WORK IN PROGRESS--

class Circles(object):
    def circumference(radius):
        pi = 3.14
        circ = 2 * pi * radius
        print("Circumference of Circle = {}".format(circ))
        
    def diameter(radius):
        dia = 2 * radius
        print("Diameter of Circle = {}".format(dia))

class Rectangles(object):
    def area(length, width):
        area = length * width
        print("Area of Rectangle = {}".format(area))

class Triangle(object):
    def area(base, height):
        area = 0.5 * base * height
        print("Area of a Triangle = {}".format(area))
