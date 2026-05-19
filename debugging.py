''' Packages &  Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''

from PIL import Image
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


print("====== (2) Package Manager & External Package ======")
''' Package manager > pip
    Python > pip pipenv
    Nodejs > npm yarn
    PHP > composer
    MacOS > brew
'''
# External package site:> https://pypi.org

with Image.open("material/images.jpeg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")


print("====== (3) Debugging ======")


def get_summary(*args):  # Define
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # find the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # Call
print("result:", result)
