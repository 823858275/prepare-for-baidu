def inOrder(root):
    if not root:
        return []
    stack=[]
    res=[]
    node=root
    while stack or node:
        while node:
            stack.append(node)
            node=node.left
        node=stack.pop()
        res.append(node.val)
        node=node.right
    return res