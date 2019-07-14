#test-graphics.py
from graphics import *

#create a Point object
p = Point(50,60)
print(p.getX())
print(p.getY())    

#create the Window object
win = GraphWin()

p.draw(win)

p2 = Point(100, 163)
p2.draw(win)

#add an oval
oval = Oval(Point(20, 150), Point(180, 199))
oval.draw(win)
oval.setFill("darkgoldenrod")

#add a rectangle
rect = Rectangle(Point(20,30), Point(180, 165))
rect.draw(win)
rect.setFill("forestgreen")

#draw a red circle
center = Point(100,100)
circ = Circle(center, 60)
circ.setFill("maroon")
circ.setOutline("dodgerblue")
circ.setWidth(5)
circ.draw(win)

#draw line
line = Line(p,p2)
line.draw(win)

#draw a second line
line2 = Line(Point(30,30), Point(80,165))
line2.draw(win)
line4 = Line(Point(170, 30), Point(120, 165))
line4.draw(win)

#adding stuff
p3 = Point(148, 60)
p4 = Point(100,163)
p3.draw(win)
p4.draw(win)

line2 = Line(p3,p4)
line2.draw(win)

line3 = Line(p,p3)
line3.draw(win)

#draw a polygon
trian = Polygon(p,p2,p3)
trian.draw(win)
trian.setFill("crimson")

#add a text label to the center of the circle
label = Text(Point(100, 175), "Mira Circulus Meum")
label.setTextColor("blue")
label.draw(win)

#draw center eye
eye = Circle(center, 20)
eye.setFill("skyblue")
eye.setOutline("white")
eye.setWidth(10)
eye.draw(win)
eyePupil = Circle(center, 10)
eyePupil.setFill("black")
eyePupil.draw(win)

#copy center eye for top right left and bottom positions
topEye = eye.clone()
topEye.move(0, -45)
topEye.setFill("saddlebrown")
topEye.draw(win)
eyePupilT = eyePupil.clone()
eyePupilT.move(0,-45)
eyePupilT.draw(win)

rightEye = eye.clone()
rightEye.move(45,0)
rightEye.setFill("olive")
rightEye.draw(win)
eyePupilR = eyePupil.clone()
eyePupilR.move(45,0)
eyePupilR.draw(win)


leftEye = eye.clone()
leftEye.move(-45,0)
leftEye.setFill("red")
leftEye.draw(win)
eyePupilL = eyePupil.clone()
eyePupilL.move(-45,0)
eyePupilL.draw(win)

botEye = eye.clone()
botEye.move(0, 45)
botEye.setFill("orchid")
botEye.draw(win)
eyePupilB = eyePupil.clone()
eyePupilB.move(0,45)
eyePupilB.draw(win)
