from typing import List
def postorderTraversal(self, root: TreeNode) -> List[int]:
    stack, node, res = [], root, []
    while stack or node:
        while node:
            stack.append(node)
            res.append(node.val)
            node = node.right  # 这里和下面交换了原版先序的顺序
        node = stack.pop()
        node = node.left  # 这里和上面交换了原版先序的顺序
    return reversed(res)