''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpaacking arguments
    (3) zip
'''

print("====== (1) What is tuple: tuple vs list ======")
# Java/PHP/NodeJs array => Python list, (array)

# Literal
numbs = [3, 5, 1, 2]
# car_dic = {"brand:": "Ferrari", "year": 1995} # bu literal usul bilan qurish
print(numbs)

# constructor (functioni orqali qurish)
letters = list("Hello World!")
# person_dict = dict(name="Adam", age=25) # bu dictionary orqali qurish
print(letters)

# list - da biz bemalol qiymatlarni update, o'zgartirsak bo'larkan
fruits = ["apple", "leomon", "banana", "kivi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# tuple - biz tuple qiymatlarlarini bir marta initiate qilganimizdan keyin qayta o'zgartira olamymiz
# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"  # bu holatda TypeError beradi chunki qiymatlarini o'zgartira olmaymizß
# print(animals)

# try avoid this
people = "Andrew", "John"
animals = "dog",


print("====== (2) Unpaacking arguments ======")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
# *z - bu usulda biz va boshqalar degan manoni tushunamiz yani bir necha qiymatni o'z cichiga oladi
# the x: y: {'FLEXY'}
# z: ['DEVEX', 'MG']
print(f"the x:", {x} and "y:", {y})
print("z:", z)  # list


# *args > tuple
def calculate(*args):  # biz *args - ni qancha qiymat qabul qilishimizni aniq bilmaganimizda ishlatamiz. qiymat noaniq bo'lsa tuple ga wrap qilamiz ekan
    print("*args", args)
    total = 1
    for x in args:
        total *= x
    # print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("-----")
calculate(0, 2, 300)
print("-----")
calculate(5, 7)

print("-----")
# **kwargs > dictionary


def introduce(**kwargs):
    # **kwargs - bizga qachonki agrumentlarimiz soni noaniq bo'lsa ishlatar ekanmiz
    print(f"the type(**kwars) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    pass


# CALL
introduce(name="Justin", age=25)
introduce(name="Shawn", age=35, single=True)


# *args, **kwargs - bizga ham typle ni ham dictionary ni unpack qilib berar ekan
def greeting(*args, **kwargs):
    print("*agrs:", args)
    print("**kwargs:", kwargs)


# Call
greeting("Hi", True, 10, name="John", age=22)

# Terminal:
# *agrs: ('Hi', True, 10)
# **kwargs: {'name': 'John', 'age': 22}


print("====== (3) zip ======")
# zip - ning vazifasi ikki tuple ni birlashtirib, bir xil indexda joylashtirib beradi
# va uni listga  taqdim etsak uni array ko'rinishida olib beradi, array-imiz ichida tuple larni hosil qilar ekan
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped:", zipped)  # terminal: zipped: <zip object at 0x107d33b00>
result = list(zipped)
print(f"the result: {result}")

# terminal:
# the result: [(1, 'a'), (2, 'b'), (3, 'c')]
