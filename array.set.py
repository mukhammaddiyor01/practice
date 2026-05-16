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
