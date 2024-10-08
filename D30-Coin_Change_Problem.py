# Day 30 
# The Coin Change Problem
def CoinsReq(coins, amount):
    s=sum(coins)+1
    dp = [s] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != s else -1

coins=[1, 2, 5]
amount=11
print("Coins required:",CoinsReq(coins, amount))  


    
