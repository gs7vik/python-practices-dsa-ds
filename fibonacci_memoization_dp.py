"""
Memoization approach(top-down approach)
#step 1: initialise dp array(n+1) with -1 
step 2: check if the subporblem has been already solved, if solved return the value of that sub problem
step 3: else compute the value and store that in the array and return it.

we are doing the following
avoiding redundant computation.
Saving previously computed results.
Reducing the time complexity from exponential O(2ⁿ) to linear O(n).
Space complexity is O(n)

"""
def fibo(n,dp):
    if n<=1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
    return dp[n]

n = 5
dp = [-1]*(n+1)

#printing 7th fibonacci number which is 13 
print(fibo(n,dp)) #13



