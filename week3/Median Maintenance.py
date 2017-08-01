from heapq import *
import sys

def MM(X):
    Total = 0
    H_high = []
    H_low = []
    for i in X:
        if len(H_high) > 0:
            if H_high[0] > i:
                heappush(H_low, -i)
            else:
                heappush(H_high, i)
        else:
            heappush(H_high, i)
        
        if len(H_high) - len(H_low) > 2:
            heappush(H_low, -(heappop(H_high)))
        elif len(H_low) == len(H_high):
            heappush(H_high, -(heappop(H_low)))
        
        Total += H_high[0]
    
    print (Total % 10000)


if __name__ == "__main__":
    file = open("quiz.txt","r")
    number = [int(l) for l in file]
    MM(number)