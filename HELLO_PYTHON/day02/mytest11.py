# 가위/바위/보를 선택하세요  가위
# 나:가위
# 컴:보
# 결과: 이김
from random import random

me = input("가위/바위/보를 선택하세요 ")
print("나: " + me)

rnd = int(random()*3);

com = ""
if rnd == 0:
    com = "가위"
    print("컴: 가위")
elif rnd == 1:
    com ="바위"
    print("컴: 바위")
elif rnd ==2:
    com = "보"
    print("컴: 보")

if me == com:
    print("결과: 무승부")
elif (me == "바위" and com == "가위") or (me == "가위" and com == "보") or (me == "보" and com == "바위"):
    print("결과: 승리")
else:
    print("결과: 패배")



