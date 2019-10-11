#后续遍历的数组最后一个值为根结点，数组的前半部分值比根节点小，后半部分值比根结点大，分别在前半部分，后半部分递归
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence==None or len(sequence)==0:
            return False
        length=len(sequence)
        root=sequence[length-1]
        for i in range(length):
            if sequence[i]>root:
                break
        for j in range(i,length):
            if sequence[j]<root:
                return False
        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[:i])
        right=True
        if i<length-1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return left and right