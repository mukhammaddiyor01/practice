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
