#设dp[n]为到第n间房的时候能偷窃到的最大金额
#则dp[n]=max(dp[n-1],dp[n-2]+num)
#因为状态转移方程只跟n的前两个状态有关，所以设置cur=dp[n-1],pre=dp[n-2]依次记录
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur=0
        pre=0
        for num in nums:
            cur,pre=max(cur,pre+num),cur
        return cur