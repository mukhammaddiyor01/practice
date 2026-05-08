# a = 147
# print("a:", a)

# message = "Hello World!"
# print(message)
# print("Hello World!")

# Pytonda mutlaqo barcha narsa object hisoblanadi

# Dunder __builtins__. Dunder bu pastki ikta chiziq _ _
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result: ", result)


''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTION > print() len() input() type()
(3) CONSTANTS > True False None

print(dir(__builtins__))    bu orqali biz builtin larning ro'yhatini ko'rishimiz mumkin ekan
'''

print(dir(__builtins__))
