from typing import List

def minSubsetSumDifference(arr: List[str], n: int) -> int:
    # write your code here
    # pass
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    #recursion solution
    # def f(i, target):

    #     if target == 0:
    #         return True
    #     if i == 0:
    #         return arr[i] == target
        
    #     not_take = f(i-1, target)

    #     take = False

    #     if target - arr[i] >= 0:
    #         take = f(i-1, target - arr[i])
        
    #     return take or not_take
    
    # f(len(arr)-1,sum/2)
    x = sum + 1
    dp = [[False]*x for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = True
    

    if arr[0] <= sum:
        dp[0][arr[0]] = True
    
    for i in range(1,len(arr)):
        for target in range(sum):
            not_take = dp[i-1][target]
            take = False
            if target-arr[i]>=0:
                take = dp[i-1][target-arr[i]]
            
            dp[i][target] = take or not_take
    
    mini = float('inf')
    for i in range(sum//2+1):

        if dp[len(arr)-1][i] == True:
            s2 = sum - i
            mini = min(mini, abs(s2-i))
    return mini
