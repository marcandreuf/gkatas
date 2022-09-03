class SingleNode:
    def __init__(self, v=None):
        self.v = v
        self.next = None

class SingleLnkdList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, position=-1):
        new_node = SingleNode(value)
        if position == -1:
            self._insert_end(new_node)
        elif position == 0:
            new_node.next = self.head
            self.head = new_node            
        else:
            node = self._get_node_at_position(position)
            if node == self.tail:
                node.next = new_node
                self.tail = new_node
            else:
                new_node.next = node.next
                node.next = new_node

    def _insert_end(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def _get_node_at_position(self, position):
        index = 0
        node = self.head
        while node is not None and index < position-1:
            if node.next is None:
                raise Exception("Error: position is out of bounds")
            node = node.next
            index += 1
        return node


    def pop(self, position = -1):
        if position == -1:            
            return self._pop_tail()
        elif position == 0:
            tmp_node = self.head
            self.head = tmp_node.next
            return tmp_node.v
        else:
            prev_node = self._get_node_at_position(position)
            tmp_node = prev_node.next
            prev_node.next = tmp_node.next
            if self.tail == tmp_node:
                self.tail = prev_node
            return tmp_node.v


    def _pop_tail(self):
        node = self.head
        if node == self.tail:
            ret = node.v
            self.head = None
            self.tail = None
        else:
            while node.next != self.tail:
                node = node.next
            ret = self.tail.v
            self.tail = node
            node.next = None
        return ret

    def peek(self, position = -1):
        if position == -1:
            return self.tail.v
        elif position == 0:
            return self.head.v
        else:
            node = self._get_node_at_position(position+1)
            return node.v

    def find(self, value):
        pos = 0
        node = self.head
        while node:
            if node.v == value:
                return pos
            else:
                node = node.next
                pos += 1
        return -1

    def delete_all(self):
        self.head = None
        self.tail = None
        

    def display(self):
        result = "["
        sep = " -> "
        suf = "]"
        node = self.head        
        while node:
            result += f"'{node.v}'{sep}"
            node = node.next
        if len(result) > 4:
            result = result[:-4]
        result += suf
        return result

    def display_all(self):
        if self.head == None:
            return "[]"
        else:
            return f"H:{self.head.v} - {self.display()} - T:{self.tail.v}"



def test_create_empty_single_list():
    sl = SingleLnkdList()
    #print(sl.display())
    #print(sl.display_all())
    assert sl.display() == "[]"
    assert sl.display_all() == "[]"
    print("test_create_empty_single_list Pass")

def test_insert_end_one_item_single_list():
    sl = SingleLnkdList()
    sl.insert('a')
    #print(sl.display())
    assert sl.display() == "['a']"
    print("test_insert_end_one_item_single_list Pass")

def test_insert_end_n_items_single_list():
    sl = SingleLnkdList()
    sl.insert('a')
    sl.insert('b')
    #print(sl.display())
    assert sl.display() == "['a' -> 'b']"
    assert sl.head.v == 'a'
    assert sl.tail.v == 'b'

    sl.insert('c')
    sl.insert('d')
    sl.insert('e')
    #print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'd' -> 'e'] - T:e"
    assert sl.head.v == 'a'
    assert sl.tail.v == 'e'
    print("test_insert_end_n_items_single_list Pass")
    
def sample_test_list():
    sl = SingleLnkdList()
    sl.insert('a')
    sl.insert('b')
    sl.insert('c')
    sl.insert('d')
    sl.insert('e')
    return sl

def test_iterate_linked_list():
    sl = sample_test_list()
    print([node.v for node in sl])
    print("test_iterate_linked_list Pass")

def test_insert_at_location():
    sl = sample_test_list()
    sl.insert('f', 3)
    #print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e'] - T:e"
    sl.insert('g', 0)
    #print(sl.display_all())
    assert sl.display_all() == "H:g - ['g' -> 'a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e'] - T:e"
    sl.insert('h', 7)
    #print(sl.display_all())
    assert sl.display_all() == "H:g - ['g' -> 'a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e' -> 'h'] - T:h"
    print("test_insert_at_location Pass")

def test_fail_insert_at_location():
    sl = sample_test_list()
    try:
        sl.insert('a', 6)
        print(f'test_fail_insert_at_location Fail. Missing expected Exception')
    except Exception as e:
        assert 'Error' in str(e), f'Expected to return Error'
        print(f'test_fail_insert_at_location PASS. Expected Exception: "{e}"')


def test_pop():
    sl = sample_test_list()
    elem = sl.pop()
    assert elem == 'e'
    #print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'd'] - T:d"
    
    sl = SingleLnkdList()
    sl.insert('a')
    elem = sl.pop()
    assert elem == 'a'
    assert sl.display_all() == "[]"
    print('test_pop Pass')

def test_peek():
    sl = sample_test_list()
    elem = sl.peek()
    assert elem == 'e'
    assert sl.tail.v == 'e'
    print('test_peek Pass')
    
def test_pop_n():
    sl = sample_test_list()
    
    elem = sl.pop(2)
    #print(sl.display_all())
    assert elem == 'c'
    assert sl.tail.v == 'e'
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'd' -> 'e'] - T:e"
    
    elem = sl.pop(0)
    #print(sl.display_all())
    assert elem == 'a'
    assert sl.head.v == 'b'
    assert sl.display_all() == "H:b - ['b' -> 'd' -> 'e'] - T:e"
    
    elem = sl.pop(2)
    #print(sl.display_all())
    assert elem == 'e'
    assert sl.head.v == 'b'
    assert sl.tail.v == 'd'
    assert sl.display_all() == "H:b - ['b' -> 'd'] - T:d"
    print('test_pop_n Pass') 

def test_peek_n():
    sl = sample_test_list()    
    elem = sl.peek(2)
    #print(sl.display_all())
    assert elem == 'c'
    elem = sl.peek(0)
    assert elem == 'a'
    elem = sl.peek(4)
    assert elem == 'e'
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'd' -> 'e'] - T:e"
    print('test_peek_n Pass')


def test_fail_pop_at_location():
    sl = sample_test_list()
    try:
        sl.pop(6)
        print(f'test_fail_pop_at_location Failed. Missing expected Exception')
    except Exception as e:
        assert 'Error' in str(e), f'Expected to return Error'
        print(f'test_fail_pop_at_location PASS. Expected Exception: "{e}"')

def test_search():
    sl = sample_test_list()
    assert sl.find('b') == 1
    assert sl.find('a') == 0
    assert sl.find('e') == 4
    assert sl.find('i') == -1
    print('test_search Pass')

def test_delete_list():
    sl = sample_test_list()
    sl.delete_all()
    assert sl.head == None
    assert sl.tail == None
    print('test_delete_list Pass')

test_create_empty_single_list()
test_insert_end_one_item_single_list()
test_insert_end_n_items_single_list()
test_iterate_linked_list()
test_insert_at_location()
test_fail_insert_at_location()
test_pop()
test_peek()
test_pop_n()
test_peek_n()
test_fail_pop_at_location()
test_search()
test_delete_list()

