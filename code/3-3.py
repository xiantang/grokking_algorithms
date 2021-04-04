def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
#
# print(fact(3))
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(4)
d = TreeNode(3)
a.left = b
b.left = c
a.right = d
def traversal(root):
    if root is None:
        return

    traversal(root.left)
    print(root.val)
    traversal(root.right)
traversal(a)