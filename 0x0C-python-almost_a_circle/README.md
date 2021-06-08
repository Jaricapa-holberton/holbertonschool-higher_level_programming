# 0x0C Python - Almost a circle

## Content

This project models a Rectangle and an Square. This class have a methods that allow create and save all created objects in a json file Rectangle.json and Square.json respectiely. Also you can read this files and create the objects.

Examples:
Save objects in json file

from models.rectangle import Rectangle

r1 = Rectangle(2, 3)
print(r1)
r1.display()

r2 = Rectangle(4, 6, 2, 3)
print(r2)
r2.display()

list_rectangles = [r1, r2]
Rectangle.save_to_file(list_rectangles)
Load objects from json files

from models.square import Squre

list_squares = Square.load_from_file()

for s in list_square:
    print(s)
    s.display()

### Files

Files
Models:(./models)
Base: Class to structure any geometry class.
Rectangle: Class to model a Rectangle object.
Square: Class to model a Square object.

Test:
test_base
test_rectangle
test_square
