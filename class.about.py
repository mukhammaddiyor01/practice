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
