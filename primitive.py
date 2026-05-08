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
