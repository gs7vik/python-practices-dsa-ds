from typing import *

  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1]*4 for _ in range(n)]

    def f(day, last,dp):
        if day==0:
            maxi = 0
            for i in range(3):
                if i!=last:
                    maxi = max(maxi,points[0][i])
            
            return maxi

        if dp[day][last]!= -1:
            return dp[day][last]   

        maxi = 0 
        for i in range(3):
            if i!= last:
                task_points = points[day][i] + f(day-1, i,dp)
                
                maxi = max(maxi, task_points)
                
        dp[day][last] = maxi
        return dp[day][last]

    x = f(len(points)-1,3,dp)
    return x 
        

            
            
        

            
    # Write your code here.
    
