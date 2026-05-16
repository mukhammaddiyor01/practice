''' Comprehension
    (1) What is comprehension & list comp 
    (2) set and dictionary comp. 
'''

print("====== (1) What is comprehension & list comp  ======")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print("list_number:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))
#  terminal
#  list_number: [1, 2, 4, 2, 1, 20]
# False
# 4380300928 4380477824


people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

cars = [
    ("ferrari", 78),
    ("Toyota", 81),
    ("Audi", 116),
    ("BMW", 109),
    ("BYD", 33)
]

list_cars = [car[0] for car in cars if car[1] > 70]  # c version
print("list_cars:", list_cars)

# terminal:
# list_cars: ['ferrari', 'Toyota', 'Audi', 'BMW']

print("====== (2) set and dictionary comp ======")

numbs = [1, 2, 4, 2, 1, 5, 4]
set_numbs = {*numbs}
print("set_nimbs:", set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dick_people:", dict_people)


# dict_people2 = {person[0]: person[1]
#                 for ad in people if person[1]}  # c bervion
# print("dick_people:", dict_poeple2)

# (<expression> for item in iterable) generic
