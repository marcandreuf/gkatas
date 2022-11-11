class AvlNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def isLeaf(self):
        return self.left == None and self.right == None

    def prt_pre_order(self):
        ret = []
        ret.append(self.data)
        if self.left:
            ret.extend(self.left.prt_pre_order())
        if self.right:
            ret.extend(self.right.prt_pre_order())
        return ret

def _sample_avl():
    avlt = AvlNode(30)
    avlt.left = AvlNode(20)
    avlt.left.left = AvlNode(10)
    return avlt

def test_create_avl_tree():
    avlt = AvlNode(30)
    assert avlt.isLeaf()

    avlt.left = _sample_avl()
    assert avlt.isLeaf() == False
    print("test_create_avl_tree PASS")

def test_pre_order_trav():
    avlt = _sample_avl()
    print(avlt.prt_pre_order())
    assert f"{avlt.prt_pre_order()}" == "[30, 20, 10]"
    print("test_pre_order_trav PASS")

def test_post_order_trav():
    print("test_post_order_trav PENDING")

def test_in_order_trav():
    print("test_in_order_trav PENDING")

def test_level_order_trav():
    print("test_level_order_trav PENDING")

test_create_avl_tree()
test_pre_order_trav()
test_post_order_trav()
test_in_order_trav()
test_level_order_trav()
