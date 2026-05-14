''' CLASSS deep diving
    (1) ENCAPSULATION 
    (2) INHERITANCE <
    (3) POLIMORPHISM <
'''

print("========  (2) INHERITANCE  ========")
# Parent > Child
# Parent only public & protected propertie(state + method) to children!


class Animal():
    # state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self.voice = voice
        self._status = "Animal is Alive"

    # method
    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):  # Child

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    # def play(self):
    #     print("Yes, I can protect you!")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the{self.name} says {self.sound}")


class Cat(Animal):  # Child

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Yes, I can play!")

    # def swim(self):
    #     print("Yes, I can swim")


class Fish(Animal):  # Child

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    # def play(self):
    #     print("Yes, I can protect you!")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("tom", "meow", True)
fish = Fish("Nemo", "Zzz", False)


dog.introduce()
cat.introduce()
fish.introduce()

print("--------")
dog.make_voice()
fish.make_voice()

print("--------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print(cat._status, cat.voice)


print("========  (3) POLIMORPHISM ========")

print("--------")
dog.make_voice()
fish.make_voice()


print("--------")
# fish > fish> animal > Object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")


# Fish > Animal > Objects

data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)

print("data", data1, data2)
