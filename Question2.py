# Question 2 

# HW 5-Question 4 (modified)



from graphics import *
import math

def makePolygon(n):
    angle = 360 / n
    vertices = []

    centerX = 250
    centerY = 250
    radius = 150

    for i in range(n):
        currentAngle = i * angle
        radians = math.radians(currentAngle)

        x = centerX + radius * math.cos(radians)
        y = centerY + radius * math.sin(radians)

        point = Point(x, y)
        vertices.append(point)

    polygon = Polygon(vertices)
    return polygon



def graphPolygon(win, entry, buttonText):
    click = win.getMouse()

    while not insideButton(click):
        click = win.getMouse()

    n = int(entry.getText())

    polygon = makePolygon(n)
    polygon.draw(win)

    buttonText.setText("Exit")
    

def insideButton(click):
    x = click.getX()
    y = click.getY()

    if 200 <= x <= 300 and 450 <= y <= 490:
        return True
    else:
        return False


def main():
    win = GraphWin("Polygon", 500, 500)

    label = Text(Point(150, 30), "Number of sides:")
    label.draw(win)

    entry = Entry(Point(300, 30), 5)
    entry.draw(win)

    button = Rectangle(Point(200, 450), Point(300, 490))
    button.draw(win)

    buttonText = Text(Point(250, 470), "Graph")
    buttonText.draw(win)

    graphPolygon(win, entry, buttonText)    

    win.getMouse()
    win.close()

main()