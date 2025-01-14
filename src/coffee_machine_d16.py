# pylint: disable=missing-module-docstring,invalid-name

from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
