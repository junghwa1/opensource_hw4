import turtle
import random

'''2019038062 염중화'''

## 변수 선언 부분 ##

myTurtle , tX, tY, tColor, tSize, tShape, tAngle= [None] * 7
playerTurtles = []
angleList = []
swidth, sheight=500, 500

## 메인 코드 부분 ##

turtle.title('거북 리스트')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

turtle.shape('turtle')
for i in range(0, 5) :
    tAngle=random.randrange(0,360)
    myTurtle = turtle
    tX = random.randrange(-swidth / 2, swidth / 2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r = random.random(); g = random.random(); b = random.random()
    tSize = random.randrange(1, 100)/10
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tAngle])

playerTurtles.sort(key=lambda x:x[3])

for tList in playerTurtles :
    myTurtle = tList[0]
    myTurtle.right(tAngle)
    myTurtle.color((tList[4], tList[5], tList[6]))
    myTurtle.pencolor((tList[4], tList[5], tList[6]))
    myTurtle.turtlesize(tList[3])
    myTurtle.goto(tList[1], tList[2])
    myTurtle.pendown()
    myTurtle.stamp()
turtle.done()
