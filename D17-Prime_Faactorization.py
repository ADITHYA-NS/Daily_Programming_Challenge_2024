#Day 17
#Prime factorization
import math
def factorize(num):
    factors=[]
    while num%2==0:
        num//=2
        factors.append(2)
    for i in range(3,int(math.sqrt(num)+1),2):
        while num%i==0:
            num=num//i
            factors.append(i)
    if num>2:
        factors.append(num)
    return factors
num=275435
print("Factors:",factorize(num))  # Output: [2, 5]
