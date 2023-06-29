# 첫수를 입력하세요 7
# 끝수를 입력하세요 9
# 7은 9보다 2만큼 작다

num1 = int(input("첫수를 입력하세요 "))
num2 = int(input("첫수를 입력하세요 "))

if num1 > num2:
    res = num1 - num2
    print("{}은(는) {}보다 {}만큼 크다".format(num1, num2, res))
elif num1 < num2:
    res = num2 - num1
    print("{}은(는) {}보다 {}만큼 작다".format(num1, num2, res))
else:
    print("같은 숫자입니다")
    
    