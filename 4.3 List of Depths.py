
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def listOfDepths(root):
    if not root:
        return []

    lvlList = []
    lvl = 0
    queue = []
    queue.append((root, lvl))

    while queue:
        node, lvl = queue.pop(0)

        if len(lvlList) == lvl:
            lvlList.append([])
        lvlList[lvl].append(node.val)
        lvl += 1

        if node.left:
            queue.append((node.left, lvl))
        if node.right:
            queue.append((node.right, lvl))
    return lvlList

def testTree():
    def addNode(x, lvl):
        if lvl > 4:
            return None
        root = TreeNode(x)
        root.left = addNode(x*2, lvl+1)
        root.right = addNode(x*2+1, lvl+1)

        return root
    return addNode(1,1)

if __name__ == '__main__':
    root = testTree()
    print(listOfDepths(root))
