#eyes.py

from graphics import *

def main():
    win = GraphWin()
    leftEye = Circle (Point(80, 50), 5)
    leftEye.setFill('yellow')
    leftEye.draw(win)
    rightEye = Circle (Point(100, 50), 5)
    rightEye.setFill('yellow')
    rightEye.draw(win)
main()
