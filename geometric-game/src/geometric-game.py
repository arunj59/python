from random import randint
import turtle


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


class GuiPoint(Point):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(10, 'red')


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


rectangle1 = GuiRectangle(Point(randint(0, 100), randint(0, 100)), Point(randint(101, 200), randint(101, 200)))

print("Rectangle Coordinates: ",
      rectangle1.point1.x, ",",
      rectangle1.point1.y, "and",
      rectangle1.point2.x, ",",
      rectangle1.point2.y)

p1 = GuiPoint(float(input("Guess value of X:")), float(input("Guess value of Y:")))

print("Your point was inside the rectangle? ", p1.falls_in_rectangle(rectangle1))

user_area = float(input("Guess area of rectangle:"))
print("Your area was off by", rectangle1.area() - user_area)

myturtle = turtle.Turtle()
rectangle1.draw(myturtle)
p1.draw(myturtle)
turtle.done()
