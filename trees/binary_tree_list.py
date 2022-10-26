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
        ret = ""
        if index > self.last:
            return ""
        else:
            ret += f"{self.btlist[index]},"
            ret += self.rec_pre_order(index*2)
            ret += self.rec_pre_order(index*2 + 1)
        return f"[{ret[:-1]}]" if index == 1 else ret

    def iter_pre_order(self):
        ret = "["
        for i in range(1, self.last):
            print(f"-------level {i}-------------")
            stack = []
            stack.append(self.btlist[i])
            while len(stack) > 0:
                print(f"stack: {stack}")
                n = stack.pop()
                print(f"poped: {n}")
                ret += f"{n},"
                l_index = i*2
                r_index = i*2+1
                if self.btlist[r_index] is not None:
                    stack.append(self.btlist[r_index])
                if self.btlist[l_index] is not None:
                    stack.append(self.btlist[l_index])
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

# test pre order traversal
# Recursive
def test_pre_order_recursive():
    bt = _traversal_btree()
    print(bt.rec_pre_order())
    assert f"{bt.rec_pre_order()}" == "[1,2,4,9,10,5,3,6,7]"
    print("test_pre_order_recursive PASS")

# Iterative
#   While index < EOL
#       https://inversepalindrome.com/blog/how-to-iteratively-traverse-a-binary-tree
def test_pre_order_iterative():
    bt = _traversal_btree()
    print(bt.iter_pre_order())
    assert f"{bt.iter_pre_order()}" == "[1,2,4,9,10,5,3,6,7]"
    print("test_pre_order_iterative PASS")
    

# test in order traversal
# test post order traversal
# test level order traversal
# test delete node


test_isEmpty_bt()
test_insert()
test_insert_full()
test_search()
test_pre_order_recursive()
test_pre_order_iterative()
