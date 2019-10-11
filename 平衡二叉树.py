class Solution:
    def IsBalanced_Solution(self, pRoot):
        self.res=True
        self.helper(pRoot)
        return self.res

    def helper(self, root):
        if not root:
            return 0
        if not self.res: return 1#已经不为二叉树提前终止该递归
        left = 1 + self.helper(root.left)#判断左子树高度，每次递归+1
        right = 1 + self.helper(root.right)#判断右子树高度，每次递归+1
        if abs(left - right) > 1:#判断每次结果
            self.res = False
        return max(left, right)#返回树的高度