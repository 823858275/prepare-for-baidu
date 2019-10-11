from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        cur=None
        for num in nums:
            if count==0:
                cur=num
            count+=1 if num==cur else -1
        return cur