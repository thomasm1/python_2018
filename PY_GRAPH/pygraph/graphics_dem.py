from graphics import *

def main():
    win = GraphWin("Xpansiv Window", 500, 500)
    win.setBackground(color_rgb( 5,40, 235))
    pt = Point(250, 250)
    cir = Circle(pt, 50)
    cir.setFill(color_rgb(113, 3, 250))
    #cir.width(5)
    cir.draw(win)
    
    rect = Rectangle(Point(450, 250), Point(250, 340))
    rect.setOutline(color_rgb(255, 100, 50))
    rect.setFill(color_rgb(255, 100, 50))
    rect.draw(win)
    
    pt.setOutline(color_rgb(3, 250, 250))
    pt1 = Point(250, 250)
    pt2 = Point(650, 1350)

    pt.draw(win)
    pt1.draw(win)
    pt2.draw(win)


    ln = Line(pt1, pt2)
    ln.setOutline(color_rgb(0, 255, 2))
    ln.draw(win)

   
    poly = Polygon(Point(40, 40),
        Point(100, 100),
        Point(50, 232),
        Point(3,3))
    poly.setFill(color_rgb(125 , 10, 150))
    poly.draw(win)

    
    txt = Text(Point(250, 250), "Xpansiv Python Graphics")
    txt.setTextColor(color_rgb(0, 255, 200))
    txt.setSize(25)
    txt.setFace('courier')
    txt.draw(win)

    rect = Rectangle(Point(450, 250), Point(250, 340))
    rect.setOutline(color_rgb(255, 100, 50))
    #rect.setFill(color_rgb(255, 100, 50))
    rect.draw(win)

    #img = Image(Point(245, 244), "radial.JPG")
    #img.draw(win)

    win.getMouse()
    win.close()

main()
