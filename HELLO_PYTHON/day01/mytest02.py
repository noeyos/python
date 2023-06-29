# 좋아하는 수를 입력하시오 4
# 또 좋아하는 수를 입력하시오 5
# 4와 5의 합은 9입니다.

num1 = int(input("좋아하는 수를 입력하시오."))
num2 = int(input("또 좋아하는 수를 입력하시오."))

sum = num1 + num2

print(num1,"와", num2,"의 합은", sum,"입니다.")
print("{}와 {}의 합은 {}입니다.".format(num1,num2,sum))