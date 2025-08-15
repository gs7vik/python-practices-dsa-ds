def ninjaTraining(n, points):
    dp = [[0] * 4 for _ in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    point = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], point)

    return dp[n - 1][3]
