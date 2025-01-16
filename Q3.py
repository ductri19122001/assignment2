import turtle as trl
l = float(input("Enter left angle: "))
r = float(input("Enter right angle: "))
len = float(input("Enter Length: "))
recursion = int(input("Enter Recursion depth: "))
reduction = float(input("Enter Branch length reduction: "))
def draw(t,l,r,len,recursion,reduction):
 if recursion == 0:
    return
 t.width(recursion)
 t.forward(len)
 t.color("green")
 t.left(l)
 draw(t,l,r,len* reduction,recursion - 1, reduction)
 t.right(r+l)
 draw(t,l,r,len* reduction,recursion - 1, reduction)
 t.left(r)
 t.penup()        
 t.backward(len) 
 t.pendown()        
screen = trl.Screen()
t=trl.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)
t.color("brown")
draw(t, l, r, len, recursion, reduction)
trl.done()

