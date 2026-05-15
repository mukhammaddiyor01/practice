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
