from turtle import Turtle,Screen
from prettytable import PrettyTable

timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("blue1")
timmy.forward(100)
print(timmy)
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)