class BinaryTreeList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.btlist = max_size * [None]
        self.last = 0
    
    def __str__(self):
        return str(self.btlist)
    
    def isEmpty(self):
        return self.last == 0

    def insert(self, value):
        pos = self.last + 1
        if pos == self.max_size:
            raise Exception('Binary tree is full')
        self.btlist[pos] = value
        self.last = pos

    def search(self, value):
        for i in range(1, self.last+1):
            if self.btlist[i] == value:
                return True
        return False

    def rec_pre_order(self, index=1):
        ret = []
        if index > self.last:
            return None
        else:
            ret.append(self.btlist[index])
            left = self.rec_pre_order(index*2)
            if left:
                ret.extend(left)
            right = self.rec_pre_order(index*2 + 1)
            if right:
                ret.extend(right)
        return ret

    def iter_pre_order(self):
        ret = []
        stack = []
        stack.append(1)
        while stack:
            idx = stack.pop()
            ret.append(self.btlist[idx])
            idx_right = idx*2+1
            idx_right = idx_right if idx_right <= self.last else None
            if idx_right:
                stack.append(idx_right)
            idx_left = idx*2
            idx_left = idx_left if idx_left <= self.last else None
            if idx_left:
                stack.append(idx_left)
        return ret



    def iter_in_order(self):
        ret = []
        stack = []
        curr_index = 1

        while curr_index or stack:
            while curr_index:
                stack.append(curr_index)
                if curr_index*2 <= self.last:
                    curr_index = curr_index*2
                else:
                    curr_index = None
            curr_index = stack.pop()
            ret.append(self.btlist[curr_index])
            if curr_index*2+1 <= self.last:
                curr_index = curr_index*2+1
            else:
                curr_index = None
                
        return ret


def test_isEmpty_bt():
    bt = BinaryTreeList(8)
    assert bt.isEmpty()
    print("test_isEmpty_bt PASS")


def test_insert():
    bt = BinaryTreeList(4)
    bt.insert("a")
    assert not(bt.isEmpty())
    print(bt)
    assert f'{bt}' == "[None, 'a', None, None]"
    print("test_insert PASS")

def _sample_btree():
    bt = BinaryTreeList(4)
    bt.insert("a")
    bt.insert("b")
    bt.insert("c")
    return bt

def test_insert_full():
    bt = _sample_btree()    
    try:
        bt.insert("d")
        print("test_insert_full FAIL. BT should be full")
    except Exception as e:
        assert 'tree is full' in str(e), f'Expected tree to be full'
        print('test_insert_full PASS')


def test_search():
    bt = _sample_btree()
    print(bt)
    assert bt.search('a')
    assert bt.search('b')
    assert bt.search('c')
    assert bt.search('d') is False
    print('test_search PASS')

def _traversal_btree():
    bt = BinaryTreeList(10)
    bt.insert("1")
    bt.insert("2")
    bt.insert("3")
    bt.insert("4")
    bt.insert("5")
    bt.insert("6")
    bt.insert("7")
    bt.insert("9")
    bt.insert("10")
    return bt

def test_pre_order_recursive():
    bt = _traversal_btree()
    print(bt.rec_pre_order())
    assert f"{bt.rec_pre_order()}" == "['1', '2', '4', '9', '10', '5', '3', '6', '7']"
    print("test_pre_order_recursive PASS")

# Iterative algorith reference
# https://inversepalindrome.com/blog/how-to-iteratively-traverse-a-binary-tree

def test_pre_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_pre_order())
    assert f"{bt.rec_pre_order()}" == "['1', '2', '4', '9', '10', '5', '3', '6', '7']"
    print("test_pre_order_iterative PASS")

def test_in_order_recursive():
    print("test_in_order_recursive PENDING")

def test_in_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_in_order())
    assert f"{bt.iter_in_order()}" == "['9', '4', '10', '2', '5', '1', '6', '3', '7']"
    print("test_in_order_iterative PASS")

def test_post_order_recursive():
    print("test_post_order_recursive PENDING")

def test_post_order_iterative():
    print("test_post_order_iterative PENDING")

def test_level_order_recursive():
    print("test_level_order_recursive PENDING")

def test_level_order_iterative():
    print("test_level_order_iterative PENDING")

def test_delete_node():
    print("test_delete_node PENDING")


test_isEmpty_bt()
test_insert()
test_insert_full()
test_search()
test_pre_order_recursive()
test_pre_order_iterative()
test_in_order_recursive()
test_in_order_iterative()
test_post_order_recursive()
test_post_order_iterative()
test_level_order_recursive()
test_level_order_iterative()
test_delete_node()

