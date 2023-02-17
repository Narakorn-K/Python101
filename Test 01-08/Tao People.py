Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.clear()
tao.left(90)
for i in range(4):
    tao.forward(100)
    tao.left(90)

    
tao.Penup()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tao.Penup()
AttributeError: 'Turtle' object has no attribute 'Penup'. Did you mean: 'penup'?
tao.penup()
tao.goto(200,200)
tao.pendown()
tao.goto(200,0)
tao.goto(150,-150)
tao.goto(0,-200)
tao.left(90)
tao.goto(0,500)
tao.goto(0,200)
tao.goto(0,200)
tao.goto(0,500)
tao.goto(150,200)
tao.clear()
tao.goto(0,0)
tao.clear()
tao.left(90)
tao.right(180)
tao.goto(150,150):tao.goto(150,200)
SyntaxError: illegal target for annotation
tao.goto(150,150)
tao.goto(150,200)
tao.goto(100,250)
tao.goto(50,250)
tao.goto(0,200)
tao.goto(-50,250)
tao.goto(-100,250)
tao.goto(-150,200)
tao.goto(-150,150)
tao.goto(0,0)
tao.undo()
tao.goto(0,0)
tao.penup()
tao.goto(0,150)
tao.pendown()
tao.goto(-50,100)
tao.undo()
tao.goto(-25,125)
tao.goto(25,75)
tao.goto(0,50)
tao.goto(-25,75)
tao.penup()
tao.goto(0,150)
tao.pendown()
tao.goto(25,125)
tao.penup
<bound method TPen.penup of <turtle.Turtle object at 0x000001C1933DE190>>
tao.penup()
tao.home()
tao.goto(-75,175)
tao.dot(5)
tao.dot(30)
tao.goto(75,175)
tao.dot(30)
tao.undo
<bound method RawTurtle.undo of <turtle.Turtle object at 0x000001C1933DE190>>
tao.undo()
tao.circle(30)
tao.right(90)
tao.fd(15)
tao.pendown()
tao.circle(15)
tao.undo()
tao.bk(15)
tao.circle(15)
tao.undo
<bound method RawTurtle.undo of <turtle.Turtle object at 0x000001C1933DE190>>
tao.undo()
tao.undo()
tao.penup()
tao.bk(15)
tao.goto(75,175)
tao.pendown()
tao.circle(15)
tao.undo()
tao.penup()
tao.goto(60,175)
tao.pendown()
tao.circle(15)
tao.home()
tao.undo()
tao.undo()
tao.penup()
tao.home()
tao.title("My Turtle First Test Python")
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    tao.title("My Turtle First Test Python")
AttributeError: 'Turtle' object has no attribute 'title'. Did you mean: 'tilt'?
tao.shape(cat)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    tao.shape(cat)
NameError: name 'cat' is not defined
tao.shape('cat')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    tao.shape('cat')
  File "C:\Python311\Lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named cat
tao.goto(0,-50)
tao.pen(pencolor="red",fillcolor="pink",pensize=10)
tao.begin_fill()
tao.circle(50)
tao.pendown()
tao.circle(50)
tao.undo()
tao.lt(90)
tao.lt(180)
tao.fd(100)
tao.circle(50)
tao.lt(180)
tao.circle(50)
tao.lt(180)
tao.fd(200)
tao.lt(90)
tao.fd(150)
tao.undo()
tao.fd(100)
tao.bk(200)
tao.rt(90)
tao.fd(50)
tao.pen(pencolor="black",pensize=2)
tao.lt(90)
tao.fd(200)
tao.undo()
tao.penup()
tao.fd(200)
tao.lt(90)
tao.pen(pencolor="red",pensize=10)
tao.pendown()
tao.fd(50)
tao.penup()
tao.fd(200)
tao.home()
tao.goto(0,-50)
tao.rt(60)
tao.pendown()
tao.fd(50)
tao.rt(120)
tao.fd(100)
tao.undo()
tao.goto(0)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    tao.goto(0)
  File "C:\Python311\Lib\turtle.py", line 1775, in goto
    self._goto(Vec2D(*x))
TypeError: turtle.Vec2D() argument after * must be an iterable, not int
tao.goto(0,-100)
tao.penup()
tao.home
<bound method TNavigator.home of <turtle.Turtle object at 0x000001C1933DE190>>
tao.home()
tao.home()

tao.undo()
tao.undo()

tao.undo()
tao.undo()
tao.undo()

tao.undo()tao.undo()tao.undo()
SyntaxError: invalid syntax
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()

tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()

tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()

tao.undo()
tao.undo()
tao.undo()
tao.undo()

tao.undo()
tao.undo()

tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.undo()
tao.home
<bound method TNavigator.home of <turtle.Turtle object at 0x000001C1933DE190>>
tao.home()
tao.rt(90)
tao.fd(50)
tao.lt(60)
tao.fd(100)
tao.lt(60)
tao.fd(100)
tao.pensize(1)
tao.lt(90)
tao.fd(15)
tao.undo()
tao.pensize(5)
tao.fd(15)
tao.bk(15)
tao.bk(15)
tao.fd(15)
tao.rt(90)
tao.fd(15)
tao.penup()
tao.home()
tao.goto(0,-50)
tao.bk(200)
tao.undo()
tao.pendown()
tao.bk(200)
tao.pensize(10)
tao.fd(200)
tao.bk(200)
tao.pensize(5)
tao.bk(15)
tao.fd(15)
tao.lt(45)
tao.undo()
tao.lt(90)
tao.fd(10_
       
SyntaxError: invalid decimal literal
tao.fd(10)
       
tao.lt(90)
       
tao.fd(15)
       
tao.bk(5)
       
tao
       
<turtle.Turtle object at 0x000001C1933DE190>
tao.rt(90)
       
tao.pensize(1)
       
tao.fd(500)
       
tao.undo()
       
tao.fd(400)
       
tao.circle(100)
       
tao.undo()
       
tao.rt(90)
       
tao.circle(100)
       
for i in range(4)
       
SyntaxError: incomplete input
for i in range(100,75,50):
       tao.circle(i)

       
for i in range(100,75,50):
       tao.circle(i)

       

c.tao.clone()
       
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    c.tao.clone()
NameError: name 'c' is not defined
c=tao.clone()
       
c=tao.clone()
       
tao.ciecle(20)
       
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    tao.ciecle(20)
AttributeError: 'Turtle' object has no attribute 'ciecle'. Did you mean: 'circle'?
for i in range(4)
       
SyntaxError: incomplete input
n=100
       
n=100
       
while n<=60:
    tao.circle(n)
    n = n+10

    
while n<=60:
    tao.circle(n)
    n = n+10

    
n=10
while n<=100:
    tao.circle(n)
    n = n+10

    
while n<=100:
    tao.circle(n)
    n = n+10t
    
SyntaxError: invalid decimal literal

tao.home()
tao.undo()
tao.undo()
tao.penup()
tao.home()
tao.goto(0,-150)
tao.rt(45)
tao.penup()
tao.fd(100)
tao.undo()
tao.pendown()
tao.fd(100)
tao.undo()
tao.pensize(10)
tao.fd(100)
tao.rt(45)
tao.fd(100)
tao.lt(50)
tao.lt(40)
tao.fd(50)
tao.penup()
tao.goto(0,-150)
tao.lt(225)
tao.fd(100)
tao.undo()
tao.pendown()
tao.fd(100)
tao.lt(45)
tao.fd(100)
tao.rt(90)
tao.fd(50)
tao.penup()
tao.bk(100)
tao.home()
tao.stamp()
40

tao.goto(0,-150)
tao.rt(90)
tao.fd(50)
tao.stamp()
41
tao.home
<bound method TNavigator.home of <turtle.Turtle object at 0x000001C1933DE190>>
>>> tao.home()
>>> n=10
>>> tao.home()
>>> tao.goto(-300,500)
>>> tao.home()
>>> tao.goto(-300,400)
>>> tao.goto(-200,350)
>>> tao.bk(15)
>>> tao.fd(5)
>>> tao.lt(90)
>>> tao.fd(100)
>>> tao.rt(90)
>>> tao.rt(180)
>>> n=10
>>> while n<=100:
...     tao.circle(n)
...     n = n+1
... 
...     
>>> tao.pendown()
>>> n=10
>>> while n<=100:
...     tao.circle(n)
...     n = n+5
... 
...     
