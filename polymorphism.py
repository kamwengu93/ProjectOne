class Shape:
    def draw(self):
        print("drawing a shape")

class Square:
    def draw(self):
        print("drawing a square")

class Rectangle:
    def draw(self):
        print("drawing a rectangle")

sh = Shape()
sq = Square()
sq.draw()
rt = Rectangle()
rt.draw()
sh.draw()