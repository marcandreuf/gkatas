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


test_isEmpty_bt()
test_insert()
test_insert_full()
test_search()
