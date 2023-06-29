# 첫수를 입력하시오. 1
# 끝수를 입력하시오. 10
# 배수를 입력하시오. 5 
# 1에서 10까지 5의 배수의 합은 15입니다.

num1 = int(input("첫수를 입력하시오."))
num2 = int(input("끝수를 입력하시오."))
num3 = int(input("배수를 입력하시오."))

arr = range(num1, (num2+1))

sum = 0
for i in arr:
    if i%num3 == 0:
        sum += i
        
print(num1,"에서",num2,"까지", num3,"의 배수의 합은", sum,"입니다.")
 