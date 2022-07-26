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
            right = self.rec_pre_order(index*2+1)
            if right:
                ret.extend(right)
        return ret

    def rec_in_order(self, index=1):
        ret = []
        if index > self.last:
            return None
        else:
            left = self.rec_in_order(index*2)
            if left:
                ret.extend(left)
            ret.append(self.btlist[index])
            right = self.rec_in_order(index*2+1)
            if right:
                ret.extend(right)
        return ret

    def rec_post_order(self, index=1):
        ret = []
        if index > self.last:
            return None
        else:
            left = self.rec_post_order(index*2)
            if left:
                ret.extend(left)
            right = self.rec_post_order(index*2+1)
            if right:
                ret.extend(right)
            ret.append(self.btlist[index])
        return ret

    def rec_level_order_list(self):
        ret = []
        for idx in range(1, self.last+1):
            ret.append(self.btlist[idx])
        return ret

    def rec_level_order(self, index=1):
        ret = []
        if index > 0 and index <= self.last:
            ret.append(self.btlist[index])
            ret.extend(self.rec_level_order(index+1))
        return ret

    def iter_pre_order(self):
        ret = []
        stack = []
        idx = 1
        stack.append(idx)
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

    def iter_post_order(self):
        ret = []
        stack = []
        out_stack = []
        idx = 1
        stack.append(idx)
        while stack:
            idx = stack.pop()            
            idx_left = idx*2 if idx*2 <= self.last else None
            if idx_left:
                stack.append(idx_left)
            idx_right = idx*2+1 if idx*2+1 <= self.last else None
            if idx_right:
                stack.append(idx_right)
            out_stack.append(idx)
        while out_stack:
            idx = out_stack.pop()
            ret.append(self.btlist[idx])
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

    def iter_level_order(self):
        ret = []
        queue = []
        idx = 1
        if len(self.btlist) > 0:
            queue.append(idx)
            while queue:
                idx = queue.pop(0)
                ret.append(self.btlist[idx])
                left = idx*2 if idx*2 <= self.last else None
                right = idx*2+1 if idx*2+1 <= self.last else None
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)                
        return ret

    def delete_node(self, value):
        idx = 1
        for idx in range(self.last+1):
            if self.btlist[idx] == str(value):
                break;
        self.btlist[idx] = self.btlist[self.last]
        self.btlist[self.last] = None
        self.last -= 1




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
    bt = _traversal_btree()
    print(bt.rec_in_order())
    assert f"{bt.rec_in_order()}" == "['9', '4', '10', '2', '5', '1', '6', '3', '7']"
    print("test_in_order_recursive PASS")

def test_in_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_in_order())
    assert f"{bt.iter_in_order()}" == "['9', '4', '10', '2', '5', '1', '6', '3', '7']"
    print("test_in_order_iterative PASS")

def test_post_order_recursive():
    bt = _traversal_btree()
    print(bt.rec_post_order())
    assert f"{bt.rec_post_order()}" == "['9', '10', '4', '5', '2', '6', '7', '3', '1']"
    print("test_post_order_recursive PASS")

def test_post_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_post_order())
    assert f"{bt.iter_post_order()}" == "['9', '10', '4', '5', '2', '6', '7', '3', '1']"
    print("test_post_order_iterative PASS")

def test_level_order_recursive():
    bt = _traversal_btree()
    print(bt.rec_level_order())
    assert f"{bt.rec_level_order()}" == "['1', '2', '3', '4', '5', '6', '7', '9', '10']"
    print("test_level_order_recursive PASS")

def test_level_order_list():
    bt = _traversal_btree()
    print(bt.rec_level_order_list())
    assert f"{bt.rec_level_order_list()}" == "['1', '2', '3', '4', '5', '6', '7', '9', '10']"
    print("test_level_order_list PASS")


def test_level_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_level_order())
    assert f"{bt.iter_level_order()}" == "['1', '2', '3', '4', '5', '6', '7', '9', '10']"
    print("test_level_order_iterative PASS")

def test_delete_node():
    bt = _traversal_btree()
    bt.delete_node(3)
    print(bt)
    assert f"{bt}" == "[None, '1', '2', '10', '4', '5', '6', '7', '9', None]"
    print("test_delete_node PASS")


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
test_level_order_list()
test_level_order_iterative()
test_delete_node()

