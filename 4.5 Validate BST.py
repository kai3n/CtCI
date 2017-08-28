class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def checkBST(root, minVal, maxVal):
    if not root:
        return True
    if minVal != None and root.val <= minVal or maxVal != None and root.val >= maxVal:
        return False
    else:
        return checkBST(root.left, minVal, root.val) and checkBST(root.right, root.val, maxVal)

def isValidBST(root):
    if not root:
        return True

    minVal = maxVal = None
    return (checkBST(root.left, minVal, root.val) and checkBST(root.right, root.val, maxVal))

isBST = True
def checkBST2(root):

    def inorder(node, prev):
        global isBST
        if node.left:
            inorder(node.left, prev)

        if prev is None:
            prev = node.val
        else:
            if root.val < prev:
                isBST = False
            prev = node.val
        print(prev)
        if node.right:
            inorder(node.right, prev)
    inorder(root, None)
    return isBST

def testTree():

    def addNode(x, lvl):
        if lvl>4:
            return None
        root = TreeNode(x)
        root.left = addNode(x*2, lvl+1)
        root.right = addNode(x*2+1, lvl+1)

        return root
    return addNode(1, 1)

if __name__ == '__main__':
    root = testTree()
    print(isValidBST(root))
    print(checkBST2(root))