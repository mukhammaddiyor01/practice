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


print("========= (4) Error handling system ==========")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    # a = car_dict.speed # car_dict ichidagi statelar ichida yo'q bo'lgan stateni qo'shsak AttributeError bo'lar ekan
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:   # No speed found: 'dict' object has no attribute 'speed'
    print("No speed found:", err)
else:
    print("Executed successfully")
finally:
    print("Final closing logic")
