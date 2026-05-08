''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & Default arguments
'''


print("========== Define (parametr) vs Call (argument) ============")
# built in function > print() type()
# Function - reusable block of code!
# instead of block {} in Java, Python uses indentation!


#  DEFINE - build, parametr
def greet(a):
    # pass  # function bo'sh bo'lsa doim pass ni qo'yib ketishimiz kerak ekan
    print(f"How do you do, {a}?")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute, argument
result1 = greet('Adam')
print("result1:", result1)

result2 = greeting("Madam")
print("result2:", result2)


print("========== Keyword & default arguments) ============")
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
# name= va age= kodni osonroq tushunish uchun hosil etildi
result3 = give_greet(name="Justin", age=28)
print("Result3:", result3)

# bu yerda faqat "John" kiritilgan age esa yo'q, age ni result4 define default qiymatdan oladi
result4 = give_greet(name="John")
print("Result3:", result4)


print("========== Scope ============")
b = 100  # 3


# Define
# Scope - ning priority degan tushunchasi mavjud ular qiymatni qayerdan olish ketma-ketligi:

def calculate(a):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# Call
calculate(5)
