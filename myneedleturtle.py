n = int(input('Enter the number of needles to be simulated : '))
s = 0 #the number of needles falling in the space between the lines in plane
import time
import random
random.seed(5)
start_time = time.clock()
#Generating the n number of pairs
x1 = []
y1 = []
for i in range(n):
    x1.append(random.uniform(-10,10))
    y1.append(random.uniform(-10,10))

#setting up the turtle environmrnt
import turtle
turtle.title('my needle drop experiment')
turtle.setworldcoordinates(-11,-11,11,11)
turtle.hideturtle()
turtle.speed(0)

#setting the lines in the plane
turtle.up()
turtle.goto(-10,10)
turtle.down()
turtle.left(90)
for i in range(21):
	turtle.sety(-turtle.position()[1])
	turtle.up()
	turtle.setx(turtle.position()[0]+1)
	turtle.down()

#initialising the x2,y2 coordinate list
x2 = []
y2 = []

#putting values in x2 y2 list and throwing the needles
for i in range(n):
    
    #moving the turtle to x1[i],yi[i]
    turtle.up()
    turtle.goto(x1[i],y1[i])
    turtle.down()
    
    #rotating the turtle to a random orientation
    turtle.lt(random.uniform(0,360))
    
    #moving the turtle to x2[i],y2[i]
    turtle.up()
    turtle.fd(1)
    turtle.down()
    
    #filling up the list of x2,y2 coordinates
    x2.append(turtle.xcor())
    y2.append(turtle.ycor())

    #moving the turle and creating the needle(looks like randomly falling)
    if int(x1[i])==0 and int(x2[i])==0:
        if max(x1[i],x2[i])>0 and min(x1[i],x2[i])<0:
            turtle.pencolor('red')
            turtle.bk(1)
        else:
            turtle.pencolor('blue')
            turtle.bk(1)
            s = s + 1
    else:
        if abs(int(x1[i])-int(x2[i])) == 0:
            turtle.pencolor('blue')
            turtle.bk(1)
            s = s + 1
        else:
            turtle.pencolor('red')
            turtle.bk(1)
#turtle.mainloop()
#calculating the probability and value of pi
probability = s/n
pie = 2/(1-probability)
end_time = time.clock()
print('The probability of needle falling in space between is ',probability)
print('The approximate value of pi is ',pie)
print('Time taken is',end_time-start_time,'seconds')
            
        
