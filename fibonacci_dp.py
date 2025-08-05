def fibo(n,dp):
    if n<=1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
    return dp[n]

n = 7
dp = [-1]*(n+1)

#printing 7th fibonacci number which is 13 
print(fibo(n,dp)) #13



