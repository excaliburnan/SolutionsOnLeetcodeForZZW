class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            minU = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            if minU == dp[i2] * 2: i2 += 1
            if minU == dp[i3] * 3: i3 += 1
            if minU == dp[i5] * 5: i5 += 1
            dp[i] = minU
        return dp[-1]
