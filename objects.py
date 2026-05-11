''' OBJECTS
    (1) What is object
    (2) Iterable object & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math  # package
from math import ceil, asin
print("========= What is Object ==========")
# An object has state and method properties
# Everything is object in Python!


print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming (Chiziqli programming) / OOP (Object Oriented Programming)
# OOP 4 CONCEPTS > Abstraction(Tormoz bosishni bilsak bo'ldi qanday ishlashini emas) | Encapsulation | Inheritance | Polimorphism
result1 = math.ceil(97.7)
# CALL # ceil() - bu raqamlarni yuqoriga yaxlitlaydi 97.7 > 98
print("result1:", result1)

result2 = ceil(98.7)  # 98.7 > 99
print(result2)
