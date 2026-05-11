print("========= (2) Iterable object & RANGE ==========")
# Iterable objectlar - takrorlanish hususiyatiga ega bo'lgan object hisoblanadi
# Iterable objects : string dict tuple list range map filter


range_obj = range(3)  # [0, 3)
print("range:", range_obj)


# text = "MIT"
for letter in "MIT":  # text:
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("========= DICTIONARY ==========")
# Dictionary in JSON object!
# states #bu to'g'ridan to'g'ri hosil qilish
person = {"name": "Justin", "age": 25, "single": True}
# bu dictionary function bilan hosil qilish
person_obj = dict(name="Juston", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

name = person_obj["name"]
print("name:", name)

# name = person_obj["hobby"] # bu usul xato ekan
# print("name2:" name2)

# method: get()
# name = person_obj("name")

# get() bizga person_obj ichidan malumot olishimizga yordam berar ekan
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

# bu del - person_obj ichidagi single keyni o'chirib yuboradi
del person_obj["single"]
for key in person_obj:  # key operatori person_obj ichidan key larni olib beradi
    print(f"the key: {key} > value {person_obj.get(key)}")
# bu usulda quyidaqa javob keladi
# the name: Juston, hobby: None and balance: 0
# the key: name > value Juston
# the key: age > value 25
