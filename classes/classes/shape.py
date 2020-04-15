
"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.

Print number of sides, area of each object and Perimeter of Circle object
"""
class Shape(object):
    def __init__(self,number_of_sides):
       self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self,base,height):
        super(Triangle, self).__init__(3) 
        self.height = height
        self.base = base

    def area(self):
        return (self.base * self.height)/2

class Rectangle(Shape):
    def __init__(self,length,width):
        super(Rectangle, self).__init__(4) 
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)
    
    def area(self):
        area = super(Square,self).area()
        return area

class Circle(Shape):
    def __init__(self,radius):
        super(Circle, self).__init__(1)
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * 3.14
        
    def perimeter(self):
        return (self.radius * 2) * 3.14

if __name__ == "__main__":
    triangle = Triangle(4,3)
    print("Area of a triangle",triangle.area())
    square = Square(9)
    print("area of a square",square.area())
    rectangle = Rectangle(6,8)
    print("area of a rectangle",rectangle.area())
    circle = Circle(5)
    print("area of a circle",circle.area())
    print("pereimeter of a circle",circle.perimeter())