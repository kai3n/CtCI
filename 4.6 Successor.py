class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def minNode(node):
    while node.left:
        node = node.left
        return node.val

def successorNode(node):

    if node.right:
        return minNode(node.right)

    parent = node.parent

    while parent and parent.right == node:
        node = parent
        parent = parent.parent

    return node