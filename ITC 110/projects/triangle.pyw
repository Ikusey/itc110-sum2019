#triangle.pyw
from graphics import *

def main():
    win = GraphWin("Draw a triangle.", 400,400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5.0, 0.5),"Click on three points")
    message.draw(win)

    #get mouse clicks from the user and draw the trangle vertices
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)
    
    p3 = win.getMouse()
    p3.draw(win)

    #draw a triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("powderblue")
    triangle.setOutline("royalblue")
    triangle.setWidth(3)
    triangle.draw(win)

    message.setText("Click anywhere in the window to quit")
    win.getMouse()
    win.close()
main()
