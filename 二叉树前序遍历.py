def preOrder(root):
    if not root:
        return []
    res=[]
    node=root
    stack=[]
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node=node.left
        node=stack.pop().right
    return res