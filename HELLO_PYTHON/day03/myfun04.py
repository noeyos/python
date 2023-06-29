import random

def printHelloBye():
    rnd = random.random()
    
    if rnd > 0.5:
        print("hello")
    else:
        print("bye")
        
        
printHelloBye()