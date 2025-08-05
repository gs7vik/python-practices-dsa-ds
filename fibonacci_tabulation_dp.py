"""
Tabulation approach(bottom-top approach)
base case to the required solution approach
step 1:  initialise dp array(n+1) with -1 
step 2: identify the base cases here it is 0 and 1 and fill the dp array with these values
step 3: look at the recursion relationship (f(n) = f(n-1) + f(n-2)) and fill the dp array from 2 to n
step 4: so now change the above relation to dp[i] = dp[i-1] + dp[i-2](converting recursion relation to tabulation) and this will always start from 2 to n
TC-> O(n)
SC-> O(n) without recursion stack
but space can be optimised to O(1) by using two variables to store the last two fibonacci numbers.
"""
n = 5
dp = [-1]*n
dp[0], dp[1] = 0, 1
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1])  #when n = 6,prints 5

#space optimised soln below
prev2 = 0
prev = 1

for i in range(2,n+1):
    curr = prev + prev2
    prev2 = prev
    prev = curr

print(prev) #prints 5
    

    
    