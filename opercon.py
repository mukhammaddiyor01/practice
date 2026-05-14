''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("====== (1) Operators ======")
# + - > >= < <= == * / is    // % += **

a = 19
b = 5

# print("a > b", a > b)
# print("a * b", a * b)
# print("a / b", a / b)


result = a // b  # // - bu orqali bo'linganda faqat butun qismni olib beradi. 3.8 > 3ni
# % - bu bo'lingandagi qolgan qoldiqni olib beradi. ya'ni 19/5=3.8(qoldiq: 4) natija 4 bo'ladi
left = a % b
print(f"The result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)


# **: **(2) - bu sonni qavs ichidagi o'ringa necha raqam qo'ysak shuncha marta o'ziga ko'paytirib berar ekan
print("b**2:", b**2)  # b*b
print("b**3:", b**3)  # b*b*b

print("="*5)  # Pythonda "=" ni ham ko'paytirsa bo'lar ekan


# == - bu belgi ikta variableni o'zaro solishtiruvchi operator hisoblanadi

c = dict(name="Adam", age=26)
d = dict(name="Adam", age=26)
e = c

# bu holatda pythonda reference emas, faqat qiymatlar solishtiriladi
print("c==d", c == d)  # only value
print(id(c), id(d), id(e))

# agar biz reference ni tekshirmoqchi bo'lsak "is" dan foydalanar ekanmiz
# data = c is d
print("c is d", c is d)
print("e is c", e is c)


print("====== (2) Condition ======")
x = 15

if x > 50:
    print("case a")
elif x > 10:
    print("case b")
else:
    print("case c")


print("====== (3) Logical Operators ======")

age = 17
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person: ", person)

# Ternary Operator
person = "adult" if age > 18 else "minor"
print("person:", person)


is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:  # not - bu yerda student bo'lmasa degan manoni anglatyapti
    print("Welcome here, do you want to be student!")
elif is_admin:
    print("Please go to this office!")
# elif is_guest or is_parent:
# elif is_guest and is_parent:
elif is_parent or is_guest:
    print("Waiting room is over there!")
else:
    print("Other case")

# or - bunda qatnashgan qiymatlarning hech bo'lasa biri true bo'lsa, mantiq True bo'ladi
# and - bunda qatnashgan qiymatlarning barchasi True bo'lsa mantiq True bo'ladi aks holda, False bo'ladi®
