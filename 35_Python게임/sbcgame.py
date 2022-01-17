import turtle as t
import random as r


playing = False
score = 0
boos = 0
warpT = 0

# 부스터
tb1 = t.Turtle()
tb1.up()
tb1.hideturtle()
tb1.speed(0)
tb1.shape("circle")
tb1.color("yellow")
tb1.goto(400,370)


tb2 = t.Turtle()
tb2.up()
tb2.hideturtle()
tb2.speed(0)
tb2.shape("circle")
tb2.color("yellow")
tb2.goto(420,370)


tb3 = t.Turtle()
tb3.up()
tb3.hideturtle()
tb3.speed(0)
tb3.shape("circle")
tb3.color("yellow")
tb3.goto(440,370)


tt = t.Turtle()
tt.shape("turtle")
tt.color("red")
tt.up()
tt.hideturtle()
tt.goto(0,300)
tt.showturtle()

ti = t.Turtle()
ti.shape("circle")
ti.color("blue")
ti.up()
ti.speed(0)
ti.hideturtle()
ti.goto(0,-300)
ti.showturtle()

ts = t.Turtle()
ts.hideturtle()
ts.up()
ts.speed(0)
ts.goto(-380,360)


def pRight():
    t.setheading(0)
def pUp():
    t.setheading(90)
def pleft():
    t.setheading(180)
def pDown():
    t.setheading(270)
    
def gamePlay():
    global playing
    global score
    global boos
    global warpT
    
    t.speed(5)
    tSpeed = score
    if tSpeed > 10:
        tSpeed = 10
        t.forward(10 + tSpeed)
    else:
        t.forward(10 + tSpeed)
    
    if r.randint(1,3) == 3: 
        eTurtle()
    
    ttSpeed = score+1
    if ttSpeed > 5:
        ttSpeed = 10
        tt.forward(5 + ttSpeed)
    else:
        tt.forward(5 + ttSpeed)
        tt.speed(ttSpeed+5)
    if t.xcor() > 420:    # 울타리
        t.goto(0,0)
    if t.xcor() < -420:
        t.goto(0,0)
    if t.ycor() > 350:
        t.goto(0,0)
    if t.ycor() < -350:
        t.goto(0,0)
    
    if t.distance(ti) < 15:   # 먹이 이동
        a = r.randint(-425, 420)  
        b = r.randint(-345, 350)
        ti.goto(a, b)
        score += 1
        tt.shapesize(score,score,score)
        ts.clear()
        ts.write("[ Score: " + str(score) + " ]", False, align="center", font=("궁서", 20))
        
    if t.distance(tt) < (score*10) + 15:   #게임오버
        scoreStr = "[ Score : " + str(score) + " ]"
        showmsg("Game Over","[ 재도전은 space ]")
        playing = False
        score = 0
        boos = 0
        warpT = 0
        tt.speed(0)
        tt.goto(0,300)
        ti.goto(0,-300)
        tt.shapesize(1,1,1)
    if playing:
        t.ontimer(gamePlay, 100)
    

    

def eTurtle():
    angle = tt.towards(t.pos())
    tt.setheading(angle)
 
def showmsg(msg1, msg2):
    t.clear()
    t.speed(0)
    t.goto(0, 140)
    t.write(msg1,False, align="center", font=("궁서", 35))
    t.goto(0, -140)
    t.write(msg2,False, align="center", font=("궁서", 35))
    t.goto(0, 0)
    
def gameStart():
    global playing
    if playing == False:
        playing = True
        t.clear()
        line()
        gamePlay()
        tb1.showturtle()
        tb2.showturtle()
        tb3.showturtle()
        
def line():
    t.hideturtle()
    t.up()
    t.goto(420, 0)
    t.pendown()
    t.goto(420, 350)
    t.goto(-425, 350)
    t.goto(-425, -345)
    t.goto(420, -345)
    t.goto(420, 0)
    t.up()
    t.goto(0, 0)
    t.showturtle()

def booster():
    if playing:
        global boos
        boos += 1
        if boos == 1:
            tb1.hideturtle()
            t.forward(200)
        elif boos == 2:
            tb2.hideturtle()
            t.forward(200)
        elif boos == 3:
            tb3.hideturtle()
            t.forward(200)
        
def warp():
    if playing:
        global warpT
        warpT += 1
        if warpT == 1:
            for x in range(15):
                t.speed(10)
                a = r.randint(-425, 420)  
                b = r.randint(-345, 350)
                t.goto(a, b)
#t.onkeypress(init, "Escape")

#t.onscreenclick(t.goto)  # 마우스 누른곳으로 이동
#t.textinput("거북이를 잡아라","거북이를 잡아라")  #text입력받는 창

t.shape("turtle")
t.title("거북이를 잡아라")


t.up()
t.onkeypress(pRight, "Right")
t.onkeypress(pUp, "Up")
t.onkeypress(pleft, "Left")
t.onkeypress(pDown, "Down")


t.onkeypress(gameStart, "space")
t.onkeypress(booster, "b")
t.onkeypress(warp, "n")

t.listen()
showmsg("거북이를 잡아라(부스터: b버튼, 워프: n)", "[ space for Start ]")

t.done()


# 실행

#while True:
    