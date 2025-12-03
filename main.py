import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fractal Tree")

# Turtle for drawing
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)  # Start facing up
t.penup()
t.goto(0, -250)  # Start at bottom center
t.pendown()

# Recursive function to draw fractal tree
def draw_branch(t, branch_length, level):
    if level == 0:
        return

    # Set color based on level
    t.pencolor(0, level/10, 0)  # green gradient
    t.pensize(level)
    
    t.forward(branch_length)
    
    # Right branch
    t.right(25)
    draw_branch(t, branch_length * 0.7, level - 1)
    
    # Left branch
    t.left(50)
    draw_branch(t, branch_length * 0.7, level - 1)
    
    # Return to original orientation
    t.right(25)
    t.backward(branch_length)

# Optional: Use turtle colormode for RGB
turtle.colormode(1.0)

# Draw the tree
draw_branch(t, branch_length=100, level=7)

screen.mainloop()
