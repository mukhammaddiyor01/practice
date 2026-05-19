''' Packages &  Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''

from turtle import Screen, Turtle, done
import turtle
print("====== (1) Python Packages & Core Package ======")
''' Python Packages/Modules: Core, File and External '''
# Core Packages > https://docs.pyhton.org/3/library

# Core package
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.circle(100)

turtle.done()


print("----")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")
