class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(self, nums):
    if not nums:
        return None
    mid = (len(nums)-1)//2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root