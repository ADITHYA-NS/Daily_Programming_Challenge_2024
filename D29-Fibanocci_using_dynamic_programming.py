# Day 29
# Fibonacci using Dynamic Programming [Memorization]

def nth_fibonacci_util(n, d):
    if n <= 1: 
        return n 
    if d[n] != -1: 
        return d[n] 
    d[n] = nth_fibonacci_util(n - 1, d) + nth_fibonacci_util(n - 2, d) 
    return d[n] 
def nth_fibonacci(n): 
    d = [-1] * (n + 1) 
    return nth_fibonacci_util(n, d) 

n = 100
result = nth_fibonacci(n) 
print("The %dth Fibonacci number is %d" % (n, result)) 
