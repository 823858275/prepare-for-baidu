class Solution:
    def TreeDepth(self, pRoot):
        count=0
        if not pRoot:
            return count
        q=[]
        q.append(pRoot)
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count+=1
        return count
