# 1~45까지 수중에서 로또를 만드세요
# range 사용

from random import random

# arr = []
# for i in range(1, 45+1):
#     arr.append(i)
arr = list(range(1,45+1))

for i in range(100):
    r = int(random()*45)
    a = arr[0]
    arr[0] = arr[r]
    arr[r] = a
    
print(arr[0:6])

# for i in range(0, 6):
#     print(arr[i], end="  ")
