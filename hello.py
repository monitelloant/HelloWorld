# connect the Turtle and random libraries (aka "modules")
import turtle, random, math

# let's make a turtle
tina = turtle.Turtle()
tina.speed(10000)

# list of colors
colors = ["pink", "blue", "purple", "green", "brown", "red"]

# random color picker

# Changed online code to different size, color, amounts, speed
rotate = int(360)


def drawCircles(t, size):
    for i in range(5):
        t.circle(size)
        size = size - 4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(turtle, 100, 5)
Steve = turtle.Turtle()
Steve.speed(10000)
Steve.color('yellow')
rotate = int(90)


def drawTriangles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawTriangles(t, size)
        t.right(360 / repeat)


drawSpecial(Steve, 100, 5)
Barry = turtle.Turtle()
Barry.speed(10000)
Barry.color('red')
rotate = int(80)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Barry, 100, 5)
Terry = turtle.Turtle()
Terry.speed(10000)
Terry.color('blue')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Terry, 100, 5)


# end of stuff i found
# draw a series of circles, size=size of first
def super_circles(size):
    for x in range(1, 11):
        color_steve()
        steve.circles(size * x)


def neg_super_circles(size):
    for x in range(1, 11):
        steve.penup()
        steve.sety(steve.ycor() - size * 2)
        steve.pendown()
        color_tina()
        steve.circles(size * x)


# AT THE END OF MY APP, I WILL USE A CONDITIONAL
# A conditional is another word for "if statement"
answer = input("What next?")
print("You just said: " + answer)
if answer == "pizza":
    print("I don't know how to draw a pizza")
elif answer == "triangle":
    print("OH, I know that one!")
    triangle(10)
elif answer == "move":
    tina.goto(random.randint(-200, 200), random.randit)
else:
    print("That is not in my commands.")
if True == True:
    print("The condition was True")

