# print("================================")
# # in Java, variable is a name storage location!
# # in Python, variable is named reference! Reference bu storage ga qaratilgan tushuncha hisoblanadi

print("=============== number =================")

count = 100
# bu type() bilan biz argument typenini tekshirsak bo'larkan
count_type = type(count)
# print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("=============== string =================")
# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")
# title() - method bu Titlelarning bosh harflarini katta qilib beradi
# print(f"the type of course: {result}")
result = course.title()
print(f"the result (2): {result}")

result = course.upper()  # bu method harflarni barchasini katta harf qilib berishadi
print(f"the result (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")
print(course)

print("=============== boolean =================")
# functions > type() input() bool() int() str(kiritilgan )
y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY: True 100 -100 "MIT"
# FALSY: False 0 "" None

# or ning vazifasi: jamlangan qiymatlarning birontasi true bo'lsa, natija true bo'lib ketadi
test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
