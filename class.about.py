''' CLASS
    (1) What is class
    (2) ordinary vs static propeties
    (3) special methods
'''


print(" ===== (1) What is class =====")
# class - blueprint for object creation!
# structure > state constructor method


class Person():
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):   # self boshqa tiillarda this. ni anglatadi
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod    # class decoratorlar orqali static methodlar tuziladi
    def explain(cls):
        print("Class: static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state property|
print("person1.name:", person1.name)

# ordinary method|
person1.introduce()
person2.say_age()

print(" ===== (2) ordinary vs static propeties =====")
# static state
new_message = Person.message
print("new_message:", new_message)


# static method|
Person.explain()


print(" ===== (3) special/magic methods =====")
# Python's most common special methods are below:
# __init__, __new__, __str__, __call__, __getitem__, __len__, __eq__


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):    # bu yerda ko'zga ko'rinmasa ham doim __new__ syntax mavjud bo'ladi
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method

    def start_engine(self):
        print(f"the {self.name} started the engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):    # bu orqali print(your_car) qilganda o'zimiz xohlagan message chiqarishimiz mumkin ekan
        return f"the car.name: {self.name} was produced in {self.year} year!"

    def __call__(self):  # __call__ orqali biz methodni functiondek chaqira olamiz ekan
        print("Object called as function!")


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()


print("------")
your_car = Car("Toyota", 2026)
print(your_car)
respnse = your_car()  # look like function
print("response:", respnse)
