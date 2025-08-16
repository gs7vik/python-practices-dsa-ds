"""
in the below case memoisation will lead in TLE(O(n**2)) so have to do tabulation
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[-1] * len(triangle[i]) for i in range(m)]

        def f(i, j):
            if i == m - 1:   # base case: last row
                return triangle[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = triangle[i][j] + f(i+1, j)
            diag = triangle[i][j] + f(i+1, j+1)
            dp[i][j] = min(down, diag)
            
            return dp[i][j]
        
        # return f(0, 0)
        dp = [[0] * len(triangle[i]) for i in range(m)]
        for j in range(len(triangle[m-1])):
            dp[m-1][j] = triangle[m-1][j]
        
        for i in range(m-2,-1,-1):
            for j in range(i,-1,-1): #in recursive soln j moved like j+1.. in tabulation it would be opposite
                #copy the recurrence derived in recursion here
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(d,dg)
        
        return dp[0][0]

