#O(n^2)dp
#dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
#dp[i]代表数组前i个数字的最长子序列长度
#两个循环，外层i=0,...,n，表示当前最长的数组
#内层循环j=0,...,i-1，依次作以下判断：
#nums[i]>nums[j]，则nums[i]可以放在nums[j]后面构成递增子序列
#nums[i]<=nums[j]，则nums[i]不能方在nums[j]后面
#初始化为全1数组
from typing import List
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         dp=[1]*(len(nums)+1)
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j]<nums[i]:
#                     dp[i]=max(dp[i],dp[j]+1)
#         return max(dp)
#dp+贪心+二分
#dp[k]以长度为k+1的子序列的末尾的最大值为该元素的值

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails, res = [0] * len(nums), 0#tail为状态转移数组，res为tails的最后更新的索引的长度
        for num in nums:
            i, j = 0, res
            while i < j:#求出第一个大于该num的tail位置
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res
print(Solution().lengthOfLIS([10,9,2,5,3,7,21,18,1]))