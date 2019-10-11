from typing import List
#01硬币，每个硬币只拿一个
#dp[i][j]=min(dp[i-1][j],dp[i-1][j-c[i]]+1)分别对应拿与不拿第i个硬币
#可以优化为一维的转移方程dp[j]=min(dp[j],dp[j-c[i]]+1)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp=[float("inf")]*(amount+1)
#         for i in range(len(coins)):
#             for j in range(amount,coins[i]-1,-1):
#                 dp[j]=min(dp[j],dp[j-coins[i]]+1)
#         return dp[amount] if dp[amount]!=float("inf") else -1

#完全背包，每个硬币可以拿无数个
#dp[i][j]=min(dp[i-1][j],dp[i][j-c[i]]+1)，不取第i个，至少取一个第i个
#优化后dp[j]=min(dp[j],dp[j-c[i]]+1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]* (amount+1)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]=min(dp[j],dp[j-coins[i]]+1)
        return dp[amount] if dp[amount]!=float("inf") else -1
print(Solution().coinChange([2],3))