# 랜덤 함수를 호출하여 0.5보다 크면 홀 아니면 짝을 출력하세요.
from random import random

rnd = random()

if rnd > 0.5 :
    print("홀")
else :
    print("짝")