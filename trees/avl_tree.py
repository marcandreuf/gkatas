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
    
    # As we can not "easily" change self when we need to rebalance the self node (root)
    # this method returns the new rebalanced tree.
    def insert(self, value):
        print(f"insert {value} on node {self.data}")
        if self.data == None:
            self.data = value
            return self
        else:
            if value < self.data:
                if self.left:
                    self.left = self.left.insert(value)                    
                else:
                    self.left = AvlNode(value)
            if value > self.data:
                if self.right:
                    self.right = self.right.insert(value)
                else:
                    self.right = AvlNode(value)
            lh = self.left.height + 1 if self.left else 0
            rh = self.right.height + 1 if self.right else 0
            self.height = max(lh, rh)
            print(f"on node {self.data} before rebalance: {self.prt_hl_order()}")
            bal_self = self._rebalance_node(self)
            print(f"on node {bal_self.data} after rebalance: {bal_self.prt_hl_order()}")
            return bal_self
            
        
    def _rebalance_node(self, node): 
        lh = 0 if node.left == None else node.left.height+1
        rh = 0 if node.right == None else node.right.height+1
        print(f"Rebalance node: {node.data} lh: {lh}, rh: {rh}")
        if abs(lh-rh) > 1:
            print(f"node {node.data} is not balanced")
            if node.left and node.left.left:
                node = self._right_rotation(node)
            if node.left and node.left.right:
                node = self._left_rotation(node)
        return node
        

    def _left_rotation(self, disb_node): #left right condition
        print(f"left {disb_node.left.data}")
        print(f"left.right {disb_node.left.right.data}")
    
    def _right_rotation(self, disb_node): #left left condition
        print(f"left {disb_node.left.data}")
        print(f"left.left {disb_node.left.left.data}")
        new_root = disb_node.left
        disb_node.left = disb_node.left.right
        new_root.right = disb_node
        lh = disb_node.left.height + 1 if disb_node.left else 0
        rh = disb_node.right.height + 1 if disb_node.right else 0
        disb_node.height = max(lh, rh)
        lh = new_root.left.height + 1 if new_root.left else 0
        rh = new_root.right.height + 1 if new_root.right else 0
        new_root.height = max(lh, rh)                
        return new_root



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

def test_insert_to_empty_tree():
    avlt = AvlNode(None)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['None(0)']"
    avlt.insert(30)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(0)']"
    avlt.insert(25)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(1)', '25(0)']"
    avlt.insert(35)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(1)', '25(0)', '35(0)']"
    avlt.insert(20)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(2)', '25(1)', '35(0)', '20(0)']"
    avlt.insert(33)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(2)', '25(1)', '35(1)', '20(0)', '33(0)']"
    print("test_insert_to_empty_tree PASS")


def test_insert_rebalance_left_left_condition():
    avlt = AvlNode(None)
    items = [30,25,35,20,10]
    for i in items:
        avlt = avlt.insert(i)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['30(2)', '20(1)', '35(0)', '10(0)', '25(0)']"
    avlt = AvlNode(None)
    items = [70,50,90,30,60,20]
    for i in items:
        avlt = avlt.insert(i)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['50(2)', '30(1)', '70(1)', '20(0)', '60(0)', '90(0)']"
    avlt = AvlNode(None)
    items = [70,50,90,30,60,80,100,20,10]
    for i in items:
        avlt = avlt.insert(i)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['70(3)', '50(2)', '90(1)', '20(1)', '60(0)', '80(0)', '100(0)', '10(0)', '30(0)']"
    print("test_insert_rebalance_left_left_condition PASS")

def test_insert_rebalance_left_right_condition():
    avlt = AvlNode(None)
    items = [70,50,90,30,60,80,100,20,25]
    for i in items:
        avlt = avlt.insert(i)
    print(avlt.prt_hl_order())
    assert f"{avlt.prt_hl_order()}" == "['70(3)', '50(2)', '90(1)', '25(1)', '60(0)', '80(0)', '100(0)', '20(0)', '30(0)']"
    print("test_insert_rebalance_left_left_condition PASS")


def _sample_left_right():
    avlt = AvlNode(None)
    items = [70,50,90,30,60,80,100,20,25]
    for i in items:
        avlt.insert(i)
    return avlt


    

test_create_avl_tree()
test_pre_order_trav()
test_post_order_trav()
test_in_order_trav()
test_level_order_trav()
test_insert_to_empty_tree()
test_insert_rebalance_left_left_condition()
test_insert_rebalance_left_right_condition()




# Getting the disbalanced node was a wrong path. It is much simpler to keep the tree balanced while recursively inserting new values. The goal is that the insert method garanties that the tree keeps balanced so it does not make sense to have insert and rotate methods. It is not good for performance and increments complexity.

# AVLNode 
# ....
#    def _update_disb_node(self, disb_node, new_node):
#        if self == disb_node:
#            return new_node
#        else:
#            queue = []
#            queue.append(self)
#            while queue:
#                e = queue.pop(0)
#                if e.left:
#                    if e.left == disb_node:
#                        e.left = new_node
#                        return self
#                    else:
#                        queue.append(e.left)
#                if e.right:
#                    if e.right == disb_node:
#                        e.right = new_node
#                        return self
#                    else:
#                        queue.append(e.right)
#
#
#    def getDisbalanced(self):
#        queue = []
#        queue.append(self)
#        while queue:
#            e = queue.pop(0)
#            lh = 0 if e.left == None else e.left.height
#            rh = 0 if e.right == None else e.right.height
#            if abs(lh-rh) > 1:                
#                print(f"Node {e.data} is disbalanced with heights: {abs(lh-rh)} left: {lh} right: {rh}")
#                return e
#            if e.left:
#                queue.append(e.left)
#            if e.right:
#                queue.append(e.right)
#        return None 

#def test_getDisbalanced_node():
#    avlt = AvlNode(30)
#    avlt.insert(25)
#    avlt.insert(35)
#    print(avlt.prt_hl_order())
#    assert avlt.getDisbalanced() == None
#    avlt.insert(20)
#    print(avlt.prt_hl_order())
#    assert avlt.getDisbalanced() == None
#    avlt.insert(10)
#    print(avlt.prt_hl_order())
#    disb = avlt.getDisbalanced()
#    assert disb != None and disb.data == 30
#    print("test_getDisbalanced_node PASS")
#
#
#def test_rebalance_left_left():
#    avlt = AvlNode(30)
#    avlt.insert(25)
#    avlt.insert(35)
#    avlt.insert(20)
#    avlt.insert(10)
#    print(avlt.prt_hl_order())
#    ravlt = avlt.rebalance()
#    print(ravlt.prt_hl_order())
#    assert f"{ravlt.prt_hl_order()}" == "['25(2)', '20(1)', '30(1)', '10(0)', '35(0)']"
#    print("test_rebalance_left_left PASS")
#
#def test_rebalance_left_right():
#    avlt = _sample_left_right()
#    print(avlt.prt_hl_order())
#    assert f"{avlt.prt_hl_order()}" == "['70(4)', '50(3)', '90(1)', '30(2)', '60(0)', '80(0)', '100(0)', '20(1)', '25(0)']"
#    #ravlt = avlt.rebalance()
#    #print(ravlt.prt_hl_order())
#    #todo assert
#    print("test_rebalance_left_right PENDING")
#    
#
#def test_get_deepest_disbalanced():
#    avlt = _sample_left_right()
#    dbn = avlt.getDisbalanced()
#    assert dbn.data == 30
#    print(f"db2.data {db2.data}")
#    print("test_get_deepest_disbalanced PENDING")

#test_getDisbalanced_node()
#test_rebalance_left_left()
#test_rebalance_left_right()
#test_get_deepest_disbalanced()


