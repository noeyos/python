def showDan(dan):
    for i in range(1,9+1):
        sum = dan * i
        print("{} * {} = {}".format(dan,i,sum))
        
showDan(7)