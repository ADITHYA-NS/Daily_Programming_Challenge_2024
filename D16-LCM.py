#Day 16
#Find LCM

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a//gcd(a,b))*b
a=123456
b=789012
print("LCM:",lcm(a,b))

