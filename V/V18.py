class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_area(self):
        return self.width * self.height


shape1 = Rectangle(12, 4)
shape2 = Rectangle(3, 7)
shape3 = Rectangle(7,12)
