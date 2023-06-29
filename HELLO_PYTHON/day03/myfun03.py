import random

def getRandomHoll():
    num = random.random()
    if (num > 0.5):
        return"홀"
    else:
        return"짝"

com = getRandomHoll()
print("com", com)