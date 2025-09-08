class Solution:
    def knapsack(self, W, val, wt):
        # code here
        dp = [[-1]*(W+1) for _ in range(len(val))]

        def f(i, w):
            if i==0:
                if wt[0] <= w:
                    return val[0]
                else:
                    return 0
            
            if dp[i][w] != -1:
                return dp[i][w]
            not_take = 0 + f(i-1,w)
            
            take = float('-inf')
            
            if wt[i] <= w:
                take = val[i] + f(i-1, w-wt[i])
            
            dp[i][w] = max(not_take, take)
            return max(not_take, take)
        
        x = f(len(val)-1, W)
        
        
        # print(dp)
        
        return x
        
        