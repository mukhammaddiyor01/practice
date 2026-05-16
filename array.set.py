''' Array & Set
    (1) Array
    (2) Set 
    (3) Specific operators with set 
    
'''
from array import array
print("====== (1) Array ======")


# Sonlarimiz ketma-ketlik hajmi juda katta bo'lsa, o'ta mahsus holatda biz "array" dan foydalanamiz 1%da
# array - strick type hisoblanadi, faqat integer bilan tuziladi
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)
# terminal:
# numbers(1): array('i', [1, 4, 5, 7, 8, 41])

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)
# terminal:
# numbers(2): array('i', [14, 1, 4, 5, 7, 8, 41, 100])

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)
# terminal
# numbers(3): array('i', [14, 1, 4, 7, 8, 41])

del numbers[0:2]
print("numbers(4);", numbers)
# terminal
# numbers(4); array('i', [4, 7, 8, 41])


print("====== (2) Set ======")
# set of unique collection without keeping order!
# set - sonlar ketma-ketligidan tashkil topgan arrayni set orqali tashkil qilsak, faqat bir marta qabul qiladi. shuning uchun unique ekan
# set - da ketma ketlik yo'q ekan
new_numbers = array("i", [1, 4, 5, 4,  7, 4, 8, 7, 5, 7, 41])
numbs_set = set(new_numbers)

print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")
# terminal:
# the numbs_set: {1, 4, 5, 7, 8, 41} and type: <class 'set'>

numbs_set.add(200)
print("numbs_set(1):", numbs_set)
# numbs_set(1): {1, 4, 5, 7, 8, 41, 200}

numbs_set.add(7)
print("numbs_set(2):", numbs_set)
# numbs_set(2): {1, 4, 5, 7, 8, 41, 200}


print("====== (3) Specific operators with set ======")
# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union - bu ikkta to'plamni alohida bitta set ga to'plab beradi
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference

print("result(1):", result1)
# terminal
# result(1): {50, 20, 40, 10}

print("result(2):", result2)
# result(2): {20}

print("result(3):", result3)
# result(3): {10, 50}

print("result(4):", result4)
# result(4): {40, 10, 50}
