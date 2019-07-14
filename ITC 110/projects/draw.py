#draw.py

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(90,90))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        newShape = shape.clone()
        dx = p.getX () - c.getX()
        dy = p.getY() - c.getY()
        newShape.move(dx,dy)
        newShape.draw(win)
    message = Text(Point(100,190), "Click again to quit")
    message.draw(win)
    win.getMouse()
    win.close()

main()
