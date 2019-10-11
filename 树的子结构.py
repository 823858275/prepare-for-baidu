class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result=False
        if pRoot1!=None and pRoot2!=None:
            if pRoot1.val==pRoot2.val:
                result=self.DoesTree1hasTree2(pRoot1,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result
    def DoesTree1hasTree2(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.DoesTree1hasTree2(pRoot1.left,pRoot2.left) and self.DoesTree1hasTree2(pRoot1.right,pRoot2.right)
