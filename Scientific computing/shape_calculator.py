class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return (
            "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        )

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(0, self.height):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self, shape):
        times = 0
        if (shape.width < self.width) and (shape.height < self.height):
            times = (self.height // shape.height) * (self.width // shape.width)
            return times
        else:
            return times


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.width = Rectangle.height = side

    def set_side(self, side):
        Rectangle.width = Rectangle.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
<<<<<<< HEAD:Scientific computing/shape_calculator.py
        return "Square(side=" + str(Rectangle.width) + ")"


obj = Rectangle(50, 8)

print(obj.get_picture())
||||||| c0b0bb4 (probability calculator complete):shape_calculator.py
        return "Square(side=" + str(Rectangle.width) + ")"
=======
        return f"Square(side={Rectangle.width})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
>>>>>>> parent of c0b0bb4 (probability calculator complete):shape_calculator.py
