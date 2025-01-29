#پروژه کارگاه فاطمه بیان ورودی403

import turtle
import time
import random

delay = 0.1

#امتیاز
score = 0
high_score = 0

#تنظیمات صفحه

wn = turtle.Screen()
wn.title("snake game")
wn.setup(width=600, height=600)
wn.bgcolor("lightgreen")
wn.tracer(0)

#سر مار
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#تنظیم غذا
food = turtle.Turtle()
colors = random.choice(['red', 'blue' , 'green'])
food.shape("circle")
food.color(colors)
food.penup()
food.goto(0,100)

#تنظيمات بدنه
segments = []



#امتیاز
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0   High Score : 0 ", align = "center", font = ("candara",24,"bold"))


#حرکت سر مار
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    
    if head.direction != "up":
        head.direction = "down"

def go_right():
    
    if head.direction != "left":
        head.direction = "right"

def go_left():
    
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
         y = head.ycor()
         head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#تعريف کليد براي کنترل مار
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#حلقه بازی
while True:
    wn.update()
    
    #چک کردن برخود به صفحه
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #حذف قسمت های بدنه
        for segment in segments:
            segment.goto(1000, 1000)
        
        #حذف لیست بدنه
        segments.clear()

        #بروززسانی امیتاز
        score = 0

        pen.clear()
        pen.write("Score: {}  High Score: {} ".format(score, high_score), align = "center", font = ("candara",24,"bold"))
        
         #بروزرسانی زمان
        delay = 0.1

    # چک کردن برخورد به غذا
    if head.distance (food) < 20:
        # رفتن غذا به مکانی رندوم
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # اضافه کردن بدنه
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        #کوتاه کردن زمان
        delay -= 0.001

        #افزایش امتیاز
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {} ".format(score, high_score), align = "center", font = ("candara",24,"bold"))

    #حرکت معکوس بدنه
    for index in range (len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
    # حرکت قسمت 0 به مکان قبلی سر
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #چک کردن برخورد سر به بدن مار
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #حذف قسمت های بدنه
            for segment in segments:
                segment.goto(1000, 1000)
            
            #حذف لیست بدنه
            segments.clear()

            #بروززسانی امیتاز
            score = 0
           
            pen.clear()
            pen.write("Score: {}  High Score: {} ".format(score, high_score), align = "center", font = ("candara",24,"bold"))    
            
            #بروزرسانی زمان
            delay = 0.1

    time.sleep(delay)

wn.mainloop()

