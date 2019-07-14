#christmas.pyw
#import graphics
from graphics import *

#setup window
win = GraphWin("Christmas", 400, 400)
win.setBackground("aqua")
win.setCoords(0.0, 0.0, 400.0, 400.0)

def snowMan():
    #set and draw snowman bottom
    snowBotPoint = Point(100, 75)
    snowBot = Circle(snowBotPoint, 75)
    snowBot.setOutline("white")
    snowBot.setFill("white")
    snowBot.draw(win)

    #set and draw snowman middle
    snowMidPoint = Point(100, 180)
    snowMid = Circle(snowMidPoint, 60)
    snowMid.setOutline("white")
    snowMid.setFill("white")
    snowMid.draw(win)

    #set and draw snowman top
    snowTopPoint = Point(100, 265)
    snowTop = Circle(snowTopPoint, 45)
    snowTop.setOutline("white")
    snowTop.setFill("white")
    snowTop.draw(win)

    #set and add decorations to snowman

    #mid snowman decorations
    coal1 = Circle(snowMidPoint, 5)
    coal1.setFill("black")
    coal1.draw(win)

    coal2 = coal1.clone()
    coal2.move(0, 20)
    coal2.draw(win)

    coal3 = coal1.clone()
    coal3.move(0, 40)
    coal3.draw(win)

    #coals top
    #eyes
    eyeLeft = Circle(snowTopPoint, 5)
    eyeLeft.setFill("black")
    eyeLeft.move(-15, 15)
    eyeLeft.draw(win)
    eyeRight = eyeLeft.clone()
    eyeRight.move(30, 0)
    eyeRight.draw(win)

    #mouth
    mouthBot = Circle(snowTopPoint, 3)
    mouthBot.move(0, -25)
    mouthBot.setFill("black")
    mouthBot.draw(win)

    mouthRight = mouthBot.clone()
    mouthRight.move(10,5)
    mouthRight.draw(win)

    mouthRight = mouthBot.clone()
    mouthRight.move(20,10)
    mouthRight.draw(win)

    mouthLeft = mouthBot.clone()
    mouthLeft.move(-10,5)
    mouthLeft.draw(win)

    mouthLeftTop = mouthBot.clone()
    mouthLeftTop.move(-20,10)
    mouthLeftTop.draw(win)

    #nose
    nose = Polygon(Point(100, 270), Point(100, 260), Point(120, 265))
    nose.setFill("orange")
    nose.draw(win)

    #hat
    brim = Rectangle(Point(55, 310), Point(145, 300))
    brim.setFill("black")
    brim.draw(win)

    hat = Rectangle(Point(65,310), Point(135, 360))
    hat.setFill("black")
    hat.draw(win)

def christmasTree():
    #set and draw tree base
    base = Rectangle(Point(275, 0), Point(325, 50))
    base.setOutline("saddlebrown")
    base.setFill("saddlebrown")
    base.draw(win)

    #set and draw tree tiers
    tier1 = Polygon(Point(200, 50), Point(399, 50), Point(300, 125))
    tier1.setFill("forestgreen")
    tier1.setOutline("forestgreen")
    tier1.draw(win)

    tier2 = Polygon(Point(220, 110), Point(380, 110), Point(300, 185))
    tier2.setFill("forestgreen")
    tier2.setOutline("forestgreen")
    tier2.draw(win)

    tier3 = Polygon(Point(240, 170), Point(360, 170), Point(300, 245))
    tier3.setFill("forestgreen")
    tier3.setOutline("forestgreen")
    tier3.draw(win)

    tier4 = Polygon(Point(260, 230), Point(340, 230), Point(300, 305))
    tier4.setFill("forestgreen")
    tier4.setOutline("forestgreen")
    tier4.draw(win)

    tier5 = Polygon(Point(280, 290), Point(320, 290), Point(300, 365))
    tier5.setFill("forestgreen")
    tier5.setOutline("forestgreen")
    tier5.draw(win)

    #set and draw tree decorations
    #star
    star = Polygon(Point(300, 360), Point(305, 370), Point(315, 375), Point(305, 380), Point(300, 390),
                   Point(295, 380), Point(285, 375), Point(295, 370))
    star.setFill("gold")
    star.setOutline("gold")
    star.draw(win)

    #baubles
    #tier1baubles
    tier1Bauble1 = Circle(Point(300, 65), 10)
    tier1Bauble1.setOutline("red")
    tier1Bauble1.setFill("gold")
    tier1Bauble1.draw(win)

    tier1Bauble2 = Polygon(Point(205,50), Point(215,60), Point(225,50), Point(215,40))
    tier1Bauble2.setFill("red")
    tier1Bauble2.setOutline("yellow")
    tier1Bauble2.draw(win)

    tier1Bauble3 = Polygon(Point(395,50), Point(385,60), Point(375,50), Point(385,40))
    tier1Bauble3.setFill("red")
    tier1Bauble3.setOutline("yellow")
    tier1Bauble3.draw(win)

    tier1Bauble4 = tier1Bauble2.clone()
    tier1Bauble4.move(40, 30)
    tier1Bauble4.draw(win)

    tier1Bauble5 = tier1Bauble3.clone()
    tier1Bauble5.move(-40, 30)
    tier1Bauble5.draw(win)

    #tier2Baubles
    tier2Bauble1 = Polygon(Point(300,115), Point(310,125), Point(300,135), Point(290,125))
    tier2Bauble1.setFill("red")
    tier2Bauble1.setOutline("yellow")
    tier2Bauble1.draw(win)

    tier2Bauble2 = Circle(Point(240, 110), 10)
    tier2Bauble2.setOutline("red")
    tier2Bauble2.setFill("gold")
    tier2Bauble2.draw(win)

    tier2Bauble3 = Circle(Point(360, 110), 10)
    tier2Bauble3.setOutline("red")
    tier2Bauble3.setFill("gold")
    tier2Bauble3.draw(win)

    tier2Bauble4 = tier2Bauble2.clone()
    tier2Bauble4.move(30, 30)
    tier2Bauble4.draw(win)

    tier2Bauble5 = tier2Bauble3.clone()
    tier2Bauble5.move(-30, 30)
    tier2Bauble5.draw(win)

    #tier3Baubles
    tier3Bauble1 = tier1Bauble1.clone()
    tier3Bauble1.move(0, 120)
    tier3Bauble1.draw(win)

    tier3Bauble2 = tier1Bauble4.clone()
    tier3Bauble2.move(0, 90)
    tier3Bauble2.draw(win)

    tier3Bauble3 = tier1Bauble5.clone()
    tier3Bauble3.move(0, 90)
    tier3Bauble3.draw(win)

    tier3Bauble4 = tier3Bauble2.clone()
    tier3Bauble4.move(30, 40)
    tier3Bauble4.draw(win)

    tier3Bauble5 = tier3Bauble3.clone()
    tier3Bauble5.move(-30, 40)
    tier3Bauble5.draw(win)

    #tier4Baubles
    tier4Bauble1 = tier2Bauble1.clone()
    tier4Bauble1.move(0, 120)
    tier4Bauble1.draw(win)

    tier4Bauble2 = tier2Bauble4.clone()
    tier4Bauble2.move(5, 90)
    tier4Bauble2.draw(win)

    tier4Bauble3 = tier2Bauble5.clone()
    tier4Bauble3.move(-5, 90)
    tier4Bauble3.draw(win)

    #tier5baubles
    tier5Bauble = tier3Bauble1.clone()
    tier5Bauble.move(0, 120)
    tier5Bauble.draw(win)
    
def main():
    snowMan()
    christmasTree()
main()
