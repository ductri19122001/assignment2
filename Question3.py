import turtle as trl
l = float(input("Enter left angle: ")) #user input
r = float(input("Enter right angle: ")) #user input
len = float(input("Enter Length: "))#user input
recursion = int(input("Enter Recursion depth: "))#user input
reduction = float(input("Enter Branch length reduction: "))#user input
def draw(t,l,r,len,recursion,reduction): #make draw function
 if recursion == 0: #when recursion reach 0 stop the program
    return
 t.width(recursion) #set width base on recursion, become smaller each looping time
 t.forward(len) #move forward by lenght and be smaller each loop
 t.color("green") #green color for branches
 t.left(l) #go left
 draw(t,l,r,len* reduction,recursion - 1, reduction) #draw  left branches and smaller each time
 t.right(r+l) #go right
 draw(t,l,r,len* reduction,recursion - 1, reduction)#draw  right branches and smaller each time
 t.left(r) #set the angle to the original before move backward
 t.penup()   #set penup when movebackward     
 t.backward(len) #move backward
 t.pendown()     #setpendown to draw again   
screen = trl.Screen()
t=trl.Turtle()
t.hideturtle()
t.speed(0)
t.left(90) #set the start angle at 90 degree
t.color("brown") #set the trunk as brown then change to green later when draw branches
draw(t, l, r, len, recursion, reduction) #draw tree
trl.done()

