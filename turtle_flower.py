import turtle

turtle.screensize(2000,1200,'Khaki')

fl_1 = turtle.Turtle()

fl_1.penup()
fl_1.setpos(-1100,-600)
fl_1.pendown()

fl_1.pensize(60)
fl_1.color('ForestGreen')
fl_1.circle(1500,50)

print(fl_1.position())

fl_1.penup()
fl_1.setpos(-120.93,-184.18)
fl_1.pendown()

fl_1.pensize(4)
fl_1.color('RoyalBlue')
fl_1.fillcolor('Magenta')

fl_1.begin_fill()
for i in range(72):
  fl_1.forward(950)
  fl_1.right(175)
fl_1.end_fill()

print(fl_1.position())

fl_1.penup()
fl_1.setpos(-500,200)
fl_1.pendown()

def curve():  
    for i in range(200):  
        fl_1.right(1)  
        fl_1.forward(1)  
   
#t. speed(3)  
fl_1.color("Red", "Crimson")  
   
fl_1.begin_fill()  
fl_1.left(140)  
fl_1.forward(111.65)  
curve()  
   
fl_1.left(120)  
curve()  
fl_1.forward(111.65)  
fl_1.end_fill() 

turtle.done()