# Question 4

height = 10
bounces = 0

win = GraphWin("Bouncing Ball", 500, 500, autoflush=False)

entry = Entry(Point(250, 250), 10)
entry.draw(win)
update()

win.getMouse()

height = float(entry.getText())
entry.undraw()

win.setCoords(0, 0, 10, height)

#point determines where the center of the ball is located
ball = Circle(Point(5, height - 0.5), 0.5)
ball.draw(win)

#initial drop
ball.move(0, -(height - 1))
update()

#repeated bounces 
while height >= 0.001:
    height = height * 0.60

    for i in range(30):
        ball.move(0, height / 30)
        update()

    for i in range(30):
        ball.move(0, -height / 30)
        update()

    bounces = bounces + 1