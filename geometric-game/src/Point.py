from random import randint

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, another_point):
        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


p1 = Point(2, 2)
p2 = Point(4, 2)

rectangle1 = Rectangle(Point(randint(1,10), randint(1,10)), Point(randint(11,20), randint(11,20)))

print("Rectangle Coordinates: ",
      rectangle1.point1.x, ",",
      rectangle1.point1.y, "and",
      rectangle1.point2.x, ",",
      rectangle1.point2.y)

p1.x = float(input("Guess value of X:"))
p1.y = float(input("Guess value of Y:"))
print("Your point was inside the rectangle? ", p1.falls_in_rectangle(rectangle1))

user_area = float(input("Guess area of rectangle:"))
print("Your area was off by", rectangle1.area() - user_area )