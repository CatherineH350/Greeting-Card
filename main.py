import turtle

#turtle.Screen() allows you to define your screen size
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("LightSalmon")

#dictionary of colors
colors = {
  "purple": "#D9A9EE",
  "pink": "#F9A6B9",
  "blue": "#A6C5DC",
  "yellow": "#FCF879",
  "green": "#7DFC79",
  "white": "#FAF3FD"
}

artist = turtle.Turtle()
artist.shape("turtle")
artist.color(colors["white"])

artist.penup()
artist.goto(0,100)

#(font-family, font-size, font-style)
style = ("Verdana", 25, "normal")
artist.write("Happy Thursday!", font = style, align = "center")

artist.goto(0,70)

name = input("Hi! What's your name? ")

style2 = ("Verdana", 15, "normal")
artist.write("Hello, " + name, font = style2, align = "center")

artist.goto(0,50)

artist.write("Thank you for being you <3", font = style2, align = "center")

artist.goto(0,30)
artist.write(".....", font = style, align = "center")

artist.hideturtle()