# 1~45까지 수중에서 로또를 만드세요
# 6개

from random import random

arr = []
# arr = [1, 2, 3, 4, 5, ... 43, 44, 45]
for i in range(1, 45+1):
    arr.append(i)

for i in range(100):
    r = int(random()*45)
    a = arr[0]
    arr[0] = arr[r]
    arr[r] = a
    
print(arr[0:6])

# for i in range(0, 6):
#     print(arr[i], end="  ")
