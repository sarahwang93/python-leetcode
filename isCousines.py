class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        thislevel = [root]
        tmp = []
        level = []
        while (len(thislevel) > 0):
            nextlevel = list()
            for n in thislevel:
                if n != None:
                    if n.left != None or n.right != None:
                        nextlevel.append(n.left)
                        nextlevel.append(n.right)
                        if (n.left != None and n.right != None):
                            tmp.append((n.val, n.left.val))
                            tmp.append((n.val, n.right.val))
                        if (n.left != None and n.right == None):
                            tmp.append((n.val, n.left.val))
                        if (n.right != None and n.left == None):
                            tmp.append((n.val, n.right.val))
                    elif n.left == None and n.right != None:
                        nextlevel.append(None)
                        nextlevel.append(n.right)
                    elif n.left != None and n.right == None:
                        nextlevel.append(n.left)
                        nextlevel.append(None)

            levellist = []
            # print(tmp)
            #
            # check whether the node in same level with different parent
            #

            if not nextlevel:
                break
            thislevel = nextlevel
            # print(thislevel)

            for i in thislevel:
                if i == None:
                    levellist.append(0)
                else:
                    levellist.append(i.val)
            # print(levellist)
            level.append(levellist)

        print(level)
        print(tmp)

        parx = 0
        pary = 0

        for le in level:
            for t in tmp:
                if t[1] == x:
                    parx = t[0]
                if t[1] == y:
                    pary = t[0]
            print(parx)
            print(pary)
            if x in le and y in le and parx != pary:
                return True

        return False

