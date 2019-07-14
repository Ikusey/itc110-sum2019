#click&type.pyw
#get mouse and key press inputs from user
from graphics import*

def main():
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        field = Text(pt, key)
        field.draw(win)
    win.close()
main()
