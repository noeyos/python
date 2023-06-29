#출력할 구구단을 입력하세요 7
# 7 * 1 = 7 ... 7 * 9 = 63

num = int(input("출력할 구구단을 입력하세요"))

sum = 0
for i in range(1,9+1):
    sum = num * i
    print("{} * {} = {}".format(num, i, sum))