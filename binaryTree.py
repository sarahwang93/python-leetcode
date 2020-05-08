import collections
from collections import deque

class TreeNode:
     def __init__(self, x, left, right):
         self.val = x
         self.left = left
         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return root
        queue = collections.deque([root])
        level = set()
        last = n_last = root
        while any(queue):
            node = queue.popleft()
            same_father = set()
            if node.left:
                level.add(node.left.val)
                queue.append(node.left)
                n_last = node.left
                same_father.add(node.left.val)
            if node.right:
                level.add(node.right.val)
                queue.append(node.right)
                n_last = node.right
                same_father.add(node.right.val)
            if x in same_father and y in same_father:
                return False
            if node == last:
                last = n_last
                if x in level and y in level:
                    return True
                level = set()
        return False

if __name__ == "__main__":
    root = [1,2,3,4]
    x =4
    y =3
    print(Solution.isCousins(root,root,x,y))