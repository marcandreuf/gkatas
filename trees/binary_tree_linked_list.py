class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def prtPreOrder(self):
        ret = f"{self.data}"
        if self.left:
            ret += f"[{self.data}_l:{self.left.prtPreOrder()}]"
        if self.right:
            ret += f"[{self.data}_r:{self.right.prtPreOrder()}]"
        return ret

    def isEmpty(self):
        return self.left == None and self.right == None

def test_create_empty_tree():
    bt = TreeNode('a')
    assert bt.isEmpty()
    print("test_create_empty_tree PASS")


def _sample_tree():
    bt = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(3)
    bt.left = l1
    bt.right = r1
    l12 = TreeNode(4)
    l1.left = l12
    return bt

def test_print_preorder():
    bt = _sample_tree()
    print(bt.prtPreOrder())
    assert f"{bt.prtPreOrder()}" == "1[1_l:2[2_l:4]][1_r:3]"
    print("test_print_tree PASS")

test_create_empty_tree()
test_print_preorder()
