#click.py

from graphics import *

def main():
    win = GraphWin("Click me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())
        p.draw(win)
    win.close()
main()
