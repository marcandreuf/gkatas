from queues.queue_linked_list import QueueLinkList

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

    def prtInOrder(self):
        ret = ""
        if self.left:
            ret = f"[{self.data}_l:{self.left.prtInOrder()}]"
        ret += f"{self.data}"
        if self.right:
            ret += f"[{self.data}_r:{self.right.prtInOrder()}]"
        return ret

    def prtPostOrder(self):
        ret = ""
        if self.left:
            ret = f"[{self.data}_l:{self.left.prtPostOrder()}]"
        if self.right:
            ret += f"[{self.data}_r:{self.right.prtPostOrder()}]"
        ret += f"{self.data}"
        return ret

    def prtLevelOrder(self):
        ret = "["
        queue = QueueLinkList()
        queue.enqueue(self)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            ret += f"{node.data}:"
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

        return f"{ret[0:-1]}]"

    def find(self, value):
        q = QueueLinkList()
        q.enqueue(self)
        while not(q.isEmpty()):
            n = q.dequeue()
            if n.data == value:
                return True
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)
        return False

    def insert(self, value):
        q = QueueLinkList()
        q.enqueue(self)
        while not(q.isEmpty()):
            n = q.dequeue()
            if n.left == None:
                n.left = TreeNode(value)
                return
            if n.right == None:
                n.right = TreeNode(value)
                return
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)

    def getDeepest(self):
        q = QueueLinkList()
        q.enqueue(self)
        while not(q.isEmpty()):
            n = q.dequeue()
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)
        return n.data

    def delete(self, value):
        del_node = None
        q = QueueLinkList()
        q.enqueue(self)
        while not(q.isEmpty()):
            n = q.dequeue()
            if n.data == value:
                del_node = n
            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)
        deepest = n
        del_node.data = value



    def isEmpty(self):
        return self.left == None and self.right == None

def test_create_empty_tree():
    bt = TreeNode('a')
    assert bt.isEmpty()
    print("test_create_empty_tree PASS")


#        1
#    2       3
#4
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
    print("test_print_preorder PASS")

def test_print_inorder():
    bt = _sample_tree()
    print(bt.prtInOrder())
    assert f"{bt.prtInOrder()}" == "[1_l:[2_l:4]2]1[1_r:3]"
    print("test_print_inorder PASS")


def test_print_postorder():
    bt = _sample_tree()
    print(bt.prtPostOrder())
    assert f"{bt.prtPostOrder()}" == "[1_l:[2_l:4]2][1_r:3]1"
    print("test_print_postrder PASS")


def test_print_levelorder():
    bt = _sample_tree()
    print(bt.prtLevelOrder())
    assert f"{bt.prtLevelOrder()}" == "[1:2:3:4]"
    print("test_print_levelorder PASS")

def test_search_levelorder():
    bt = _sample_tree()
    assert bt.find(3) == True
    assert bt.find(5) == False
    print("test_search_levelorder PASS")


def test_insert_levelorder():
    bt = _sample_tree()
    bt.insert(5)
    print(bt.prtPreOrder())
    assert f"{bt.prtPreOrder()}" == "1[1_l:2[2_l:4][2_r:5]][1_r:3]"
    bt.insert(6)
    print(bt.prtPreOrder())
    assert f"{bt.prtPreOrder()}" == "1[1_l:2[2_l:4][2_r:5]][1_r:3[3_l:6]]"
    print("test_insert_levelorder PASS")


def test_get_deepest_node():
    bt = _sample_tree()
    dn = bt.getDeepest()
    assert dn == 4
    print("test_get_deepest_node PASS")

def test_delete_node():
    bt = _sample_tree()
    bt.delete(2)
    assert f"{bt.prtPreOrder()}" == "1[1_l:4][1_r:3]"
    print("test_delete_node PASS")

test_create_empty_tree()
test_print_preorder()
test_print_inorder()
test_print_postorder()
test_print_levelorder()
test_search_levelorder()
test_insert_levelorder()
test_get_deepest_node()
#test_delete_node()
