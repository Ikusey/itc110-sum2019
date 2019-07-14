#archery.py

from graphics import *

def main():
    win = GraphWin()
    win.setBackground("pink")
    center = Point(100,100)
    white = Circle(center, 85)
    white.setOutline("white")
    white.setWidth(20)
    white.draw(win)
    black = Circle(center, 65)
    black.setOutline("black")
    black.setWidth(20)
    black.draw(win)
    blue = Circle(center, 46)
    blue.setOutline("blue")
    blue.setWidth(20)
    blue.draw(win)
    red = Circle(center, 27)
    red.setOutline("red")
    red.setWidth(20)
    red.draw(win)
    yellow = Circle(center, 20)
    yellow.setFill("yellow")
    yellow.setOutline("yellow")
    yellow.draw(win)
main()
