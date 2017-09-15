from turtle import *
import time
import random
import copy

t = Turtle()
ts = t.getscreen()
ts.tracer(10)
t.hideturtle()

c = ts.getcanvas()

sd = 0
goal = random.randint(50, 200)

tlist = []

h = Turtle()
hs = h.getscreen()
mlist = []

sc = random.choice(["midnight blue", "sky blue"])
ts.bgcolor(sc)

for i in range(random.randint(60, 90)):
	t = Turtle()
	ts = t.getscreen()
	t.setheading(270)
	ts.tracer(0)
	tlist.append(t)
	t.penup()
	t.goto(random.randint(-375, 375), random.randint(300, 900))
	t.shapesize(0.3, 0.3, 0)
	t.pencolor("black")
	t.color("snow")

for i in range(random.randint(4, 7)):
	templist = []
	colors = ["snow", "light gray", "grey", "dark gray"]
	c = random.choice(colors)
	temp = copy.deepcopy(colors)
	temp.remove(c)
	t = Turtle()
	t.shape("triangle")
	t.setheading(90)
	ts = t.getscreen()
	templist.append(t)
	t.pencolor(c)
	t.color(random.choice(temp))
	t.penup()
	t.goto(random.randint(-350, 350), -350)
	a = random.randint(12, 60)
	b = random.randint(7, 17)
	t.shapesize(a, b, 5)
	templist.append([a, b, ts])
	templist.append(t.position()[1])
	mlist.append(templist)


def mountainbreak(l):
	direction = random.choice([-1])
	h = direction * 90
	l[0].settiltangle(direction * 90)
	l[1][-1].tracer(1)
	while(l[0].position()[1] > -500):
		h -= direction * 0.5
		l[0].setheading(h + direction * 90)
		l[0].forward(20)
	l[1][-1].tracer(0)

	l[0].setheading(180)
	l[0].goto(random.randint(-350, 350), -400)
	l[0].forward(0)
	

def moon():
	if sc == "sky blue":
		m.pencolor("gold")
		m.color("yellow")
	else:
		m.color("light gray")
		m.pencolor("dark gray")
	m.shape("circle")
	m.shapesize(8, 8, 0)
	m.penup()
	m.goto(-230, 230)
	m.pensize(20)
	m.stamp()
	if sc == "sky blue":
		spots = 0
	else:
		m.color("gainsboro")
		m.pencolor("gainsboro")
		spots = random.randint(3, 5)
	for i in range(spots):
		b = random.randrange(1, 3)
		m.penup()
		m.shapesize(b, b, 0)
		m.goto(random.randint(-50,50) - 230, random.randint(-50, 50) + 230)
		m.stamp()

m = Turtle()
ms = m.getscreen()
ms.tracer(0)
moon()

while True:
	for t in tlist:
		t.shape("circle")
		t.forward(random.randint(4, 10))
		t.left(random.randint(0, 5))
		t.right(random.randint(0, 5))
		if t.heading() < 180:
			t.setheading(270)
		elif t.heading() > 360:
			t.setheading(270)
		if t.ycor() < -300:
			t.hideturtle()
			t.goto(random.randint(-375, 375), random.randint(300, 400))
			t.showturtle()
			sd += 1
		if sd >= goal:
			for m in mlist:
				if m[2] > -200:
					#mountainbreak(m)
					'''
					m[0].goto(random.randint(-350, 350), -350)
					a = random.randint(12, 60)
					b = random.randint(7, 17)
					m[0].shapesize(a, b, 5)
					'''
					
				else:
					m[1][1] += 0.2
					m[1][0] += 0.2
					m[0].shapesize(m[1][0], m[1][1], 5)
					m[2] += 3
			sd = 0
			goal = random.randint(50, 200)
		
	ts.update()

