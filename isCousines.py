class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        thislevel = [root]

        while (len(thislevel) > 0):
            nextlevel = list()
            tmplist = list()
            for n in thislevel:
                if n != None:
                    if n.left != None or n.right != None:
                        nextlevel.append(n.left)
                        nextlevel.append(n.right)
                    elif n.left == None and n.right != None:
                        nextlevel.append(None)
                        nextlevel.append(n.right)
                    elif n.left != None and n.right == None:
                        nextlevel.append(n.left)
                        nextlevel.append(None)

            levellist = []
            for i in nextlevel:
                if i == None:
                    levellist.append(0)
                else:
                    levellist.append(i.val)

            # check whether the node in same level with different parent
            if x in levellist and y in levellist and:

            if not nextlevel:
                break
            thislevel = nextlevel
            print(thislevel)

        return False

