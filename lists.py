''' List
    (1) Working with lists
    (2) List Methods 
    (3) Lambda function 
    (4) enumarate, map and filter
'''

print("====== (1) Working with lists ======")
# Java/ PHP/ NodeJs array => Python list


# Literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello World!")
print(f"the letters: {result} and size: {len(result)}")


print("-----")
fruits = ["apple", "orange", "lemon", "kiwi"]


a = fruits[0]
b = fruits[0:2]
# 0:2 - ning manosi 0dan boshlab 2 gacha bo'lgan qiymatlarni olib ber degani. lekin 2 kirmaydi [0, 2)
c = fruits[::3]
# ::3 - buni manosi o-indexni ol hamda 3marta sakrab 3-indexni qiymatini olib beradi
d = fruits[::-1]
# ::-1 - buni manosi qiymatni teskari sanab beradi
# d: ['kiwi', 'lemon', 'orange', 'apple']

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# terminal:
# a: apple
# b: ['apple', 'orange']
# c: ['apple', 'kiwi']
# d: ['kiwi', 'lemon', 'orange', 'apple']


print("====== (2) List Methods ======")
# methods > append() insert() pop() remove() clear() sort()  - mutable | index()- immutable

letters = ["a", "d", "b"]


letters.append("c")  # add behind
# bu method array ohiridan yangi qiymat qo'shadi
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")


size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters} ")
# terminal: the pop result1: c and letters: ['z', 'a', 'd', 'b']


result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and lettters: {letters}")
# terminal: the pop result2: z and lettters: ['a', 'd', 'b']


print("--------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)


animals.remove("lion")
# terminal: animals remove: ['dog', 'cat', 'capybara', 'fish']
print("animals remove:", animals)

del animals[2:4]
# terminal: animals delete: ['dog', 'cat']
print("animals delete:", animals)

# index() - bu arrayimiz ichida index bor yo'qligini tekshirib berar ekan
exist = animals.index("cat")  # terminal: animals exist: 1
print("animals exist:", exist)

# clear() - bu barcha qiymatni o'chirib yubradi
animals.clear()
print("animals clear:", animals)  # terminal: animals clear: []


if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("---------")
# sort() - bu tartiblab beradi katta kichikligini
numbers = [2, 20, 12, 8, 57]
numbers.sort()  # terminal: numbers: [2, 8, 12, 20, 57]
print("sort default:", numbers)
numbers.sort(reverse=True)  # terminal: sort reverse: [57, 20, 12, 8, 2]
print("sort reverse:", numbers)


# immutable sorted(iterable, key=key, reverse=reverse)
# sorted() - bu numbs ni yangi numbs ga tenglab, new_numbs dagi qiymatnigina o'zgartiradi. numbs o'zgarmaydi
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
# terminal: the sorted numbs: [2, 20, 12, 100] and new_numbs: [2, 12, 20, 100]
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("====== (3) Lambda function ======")
# lamba is small anonymous function!
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)
# terminal: result: 15

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]
people.sort()
print("people(1):", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)

# terminal:
# people(1): [('Ali', 40), ('Joseph', 25), ('Michael', 30), ('Robert', 20), ('Steve', 19)]
# people(2) [('Steve', 19), ('Robert', 20), ('Joseph', 25), ('Michael', 30), ('Ali', 40)]


print("====== (4) enumerate, map and filter ======")
# enumerate(iterable, start) for index & value

animals = ["dog", "cat"]
for element in enumerate(animals):
    print("element:", element)
# terminal:
# element: (0, 'dog')
# element: (1, 'cat')
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")
# terminal:
# the index: 0 and value: dog
# the index: 1 and value: cat

print("---------")
# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)  # dict
# result = car_obj.get("brand")
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and value: {value}")
# terminal:
# the key: brand and value: Ferrari
# the key: year and value: 2025

print("---------")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87,),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car", new_cars)

result_map = map(lambda car: car[0], cars)
print(f"result1: {result_map} and type: {type(result_map)}")
# terminal:
# result1: <map object at 0x1098bfb00> and type: <class 'map'>

new_cars = list(result1)
print("new_cars(2)", new_cars)
# terminal:
# new_cars(2) ['c']


print("---------")
# filter(function, iterable)
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_map)}")
print(list(result_filter))
# terminal:
# the result_filter: <filter object at 0x102636e00> and type: <class 'map'>
# [('Toyota', 87), ('Audi', 116), ('BMW', 109)]
