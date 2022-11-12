class AvlNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

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

    def prt_post_order(self):
        ret = []
        if self.left:
            ret.extend(self.left.prt_post_order())
        if self.right:
            ret.extend(self.right.prt_post_order())
        ret.append(self.data)
        return ret

    def prt_in_order(self):
        ret = []
        if self.left:
            ret.extend(self.left.prt_in_order())
        ret.append(self.data)
        if self.right:
            ret.extend(self.right.prt_in_order())
        return ret

    def prt_level_order(self):
        ret = []
        queue = []
        queue.append(self)
        while queue:
            e = queue.pop(0)
            ret.append(e.data)
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
        return ret

    def prt_hl_order(self):
        ret = []
        queue = []
        queue.append(self)
        while queue:
            e = queue.pop(0)
            ret.append(f"{e.data}({e.height})")
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
        return ret



    def insert(self, value):
        if self.data == None:
            self.data = value
        else:
            if value < self.data:
                if self.left:
                    self.left.insert(value)
                    self.height = self.left.height + 1
                else:
                    self.left = AvlNode(value)
                    self.height = 1
            if value > self.data:
                if self.right:
                    self.right.insert(value)
                    self.height = self.right.height + 1
                else:
                    self.right = AvlNode(value)
                    self.height = 1
                self.right = AvlNode(value)

    def isBalanced(self):
        queue = []
        queue.append(self)
        while queue:
            e = queue.pop(0)
            lh = 0 if e.left == None else e.left.height
            rh = 0 if e.right == None else e.right.height
            if (e.height > lh+1) or (e.height > rh+1):
                print(f"{e.height} {lh} {rh}")
                return False
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
        return True

def _sample_avl():
    avlt = AvlNode(30)
    avlt.left = AvlNode(20)
    avlt.left.left = AvlNode(10)
    avlt.left.right = AvlNode(25)
    avlt.right = AvlNode(40)
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
    assert f"{avlt.prt_pre_order()}" == "[30, 20, 10, 25, 40]"
    print("test_pre_order_trav PASS")

def test_post_order_trav():
    avlt = _sample_avl()
    print(avlt.prt_post_order())
    assert f"{avlt.prt_post_order()}" == "[10, 25, 20, 40, 30]"
    print("test_post_order_trav PASS")

def test_in_order_trav():
    avlt = _sample_avl()
    print(avlt.prt_in_order())
    assert f"{avlt.prt_in_order()}" == "[10, 20, 25, 30, 40]"
    print("test_in_order_trav PASS")

def test_level_order_trav():
    avlt = _sample_avl()
    print(avlt.prt_level_order())
    assert f"{avlt.prt_level_order()}" == "[30, 20, 40, 10, 25]"
    print("test_level_order_trav PASS")

def test_insert_to_enpty_tree():
    avlt = AvlNode(None)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['None(0)']"
    avlt.insert(30)
    assert f"{avlt.prt_hl_order()}" == "['30(0)']"
    avlt.insert(25)
    assert f"{avlt.prt_hl_order()}" == "['30(1)', '25(0)']"
    avlt.insert(35)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(1)', '25(0)', '35(0)']"
    avlt.insert(20)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(2)', '25(1)', '35(0)', '20(0)']"
    print("test_insert_to_enpty_tree PASS")


def test_isBalanced_tree():
    avlt = AvlNode(None)
    avlt.insert(30)
    avlt.insert(25)
    avlt.insert(35)
    print(avlt.prt_hl_order())
    assert avlt.isBalanced()
    avlt.insert(20)
    print(avlt.prt_hl_order())
    assert avlt.isBalanced() == False
    print("test_isBalanced_tree PASS")

test_create_avl_tree()
test_pre_order_trav()
test_post_order_trav()
test_in_order_trav()
test_level_order_trav()
test_insert_to_enpty_tree()
test_isBalanced_tree()
