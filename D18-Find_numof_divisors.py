#Day 18
#Count Number of Divisors
import math
def NumDivisor(num):
    if num==1:
        return 1
    count=0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            count+=1
            if i!=num//i:  
                count+=1
    return count
num=12
print("Number of Divisors:",NumDivisor(num))
                   
