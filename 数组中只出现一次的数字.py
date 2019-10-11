class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        tmp=0
        for i in array:
            tmp^=i
        idx=0
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a=b=0
        for i in array:
            if self.isBit(i,idx):
                a^=i
            else:
                b^=i
        return [a,b]
    def isBit(self,num,idx):
        num = num >> idx
        return num & 1