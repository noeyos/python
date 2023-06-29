# 홀/짝을 선택하세요 홀
# 나 : 홀
# 컴 : 홀
# 결과: 승리/패배(똑같으면 이김, 다르면 짐)
from random import random

me = input("홀/짝을 선택하세요")
print("나 : " + me)
rnd = random()
if rnd > 0.5:
    com = "홀"
    print("컴 : " + com)
else:
    com = "짝"
    print("컴 : " + com)

if me == com:
    print("== 승리 ==")
else:
    print("== 패배 ==")