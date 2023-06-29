# 1에서 9까지 수 중에서 중복없이 섞어서 3개의 수를 출력하세요
from random import random

arr = [1,2,3,4,5,6,7,8,9]

for i in range(100):
    r = int(random()*9)
    a = arr[0]
    arr[0] = arr[r]
    arr[r] = a

print(arr[0], arr[1], arr[2])
# random.shuffle(arr)
#
# newarr = []
# #rndarr = []
# for i in range(0,3):
#     rnd = int(random.random()*10)
#     if arr[rnd] in newarr:
#         continue
#     else:
#         newarr.append(arr[rnd])
#
# print(newarr)