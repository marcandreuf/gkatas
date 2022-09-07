class DoubleNode:
    def __init__(self, v=None):
        self.v = v
        self.prev = None
        self.next = None

class CircDoubleLnkdList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node.next != self.head:
            yield node
            node = node.next
        yield self.tail
    
    
    def insert(self, value, position=-1):
        new_node = DoubleNode(value)
        if position == -1:
            return self._insert_end(new_node)
        elif position == 0:
            tmp = self.head
            new_node.next = tmp
            self.head = new_node
            new_node.prev = tmp.prev
            tmp.prev = new_node
            self.tail.next = new_node
        else:
            node = self._get_node_at_position(position)
            if node == self.tail:
                tmp = self.tail
                new_node.next = tmp.next
                tmp.next = new_node
                new_node.prev = tmp
                self.tail = new_node
                self.head.prev = new_node
            else:
                new_node.next = node
                new_node.prev = node.prev
                node.prev = new_node
                new_node.prev.next = new_node
       
    def pop(self, position=-1):
        if position == -1:
            return self._pop_tail()
        elif position == 1:
            ret_value = self.head.v
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            return ret_value
        else:
            node = self._get_node_at_position(position)
            if node == self.tail:
                return self._pop_tail()
            else:
                ret_value = node.v
                node.prev.next = node.next
                node.next.prev = node.prev
                return ret_value


        return ret_value

    def _pop_tail(self):
        ret_value = self.tail.v
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        return ret_value

    def peek(self, position=-1):
        if position == -1:
            return self.tail.v
        elif position == 1:
            return self.head.v
        else:
            node = self._get_node_at_position(position)
            return node.v

    def find(self, value):
        if self.head == None:
            return -1
        else:
            node = self.head
            if node.v == value:
                return 1
            node = node.next
            index = 2
            while node is not self.head:
                if node.v == value:
                    return index
                index += 1
                node = node.next
            return -1

    def delete_all(self):
        self.tail.next = None
        self.head.prev = None
        self.head = None
        self.tail = None


    def _get_node_at_position(self, position):
        index = 0
        node = self.head
        while node is not self.tail and index < position-1:
            node = node.next
            index += 1
        if position < 1 or position > index+2:
            raise Exception("Error: position is out of bounds")
        return node


    def _insert_end(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tmp = self.tail
            tmp.next = new_node
            new_node.prev = tmp
            self.tail = new_node
            new_node.next = self.head
            self.head.prev = new_node



    def __str__(self):
        if self.head == None:
            return '[]'
        else:
            return f"H={self.head.v} {self._print_list()} T={self.tail.v}"
        

    def _print_list(self):
        if self.head == None:
            return '[]'
        else:
            sep = ' -> '
            suf = ']'
            result = '['
            node = self.head
            while True:
                result += f"'{node.prev.v}:{node.v}:{node.next.v}'{sep}"
                if node.next == self.head:
                    break
                else:
                    node = node.next
            if len(result) > 4:
                result = result[:-4]
            return result + suf

def test_create_empty_circ_double_lnkd_list():
    cdl = CircDoubleLnkdList()
    print(cdl)
    assert f"{cdl}" == '[]'
    print('test_create_empty_circ_double_lnkd_list PASS')


def test_insert_end_one_item_circ_double_lnkd_list():
    cdl = CircDoubleLnkdList()
    cdl.insert('a')
    print(cdl)
    assert f"{cdl}" == "H=a ['a:a:a'] T=a"
    print('test_insert_end_one_item_double_lnkd_list PASS')
    

def test_insert_end_n_items_circ_double_lnkd_list():
    cdl = CircDoubleLnkdList()
    cdl.insert('a')
    cdl.insert('b')
    cdl.insert('c')
    print(cdl)
    assert f"{cdl}" == "H=a ['c:a:b' -> 'a:b:c' -> 'b:c:a'] T=c"
    print('test_insert_end_n_items_circ_double_lnkd_list PASS')


def sample_list():
    cdl = CircDoubleLnkdList()
    cdl.insert('a')
    cdl.insert('b')
    cdl.insert('c')
    cdl.insert('d')
    cdl.insert('e')
    return cdl


def test_iterate_circ_double_lnkd_list():
    cdl = sample_list()
    print([node.v for node in cdl])
    print('test_iterate_circ_double_lnkd_list PASS')

    
def test_insert_at_location():
    cdl = sample_list()
    print(cdl)
    assert f"{cdl}" == "H=a ['e:a:b' -> 'a:b:c' -> 'b:c:d' -> 'c:d:e' -> 'd:e:a'] T=e"
    
    cdl.insert('f', 3)
    print(cdl)
    assert f"{cdl}" == "H=a ['e:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:a'] T=e"
    
    cdl.insert('g', 0)
    print(cdl)
    assert f"{cdl}" == "H=g ['e:g:a' -> 'g:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:g'] T=e"
    
    cdl.insert('h', 8)
    print(cdl)
    assert f"{cdl}" == "H=g ['h:g:a' -> 'g:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:h' -> 'e:h:g'] T=h"    

def test_fail_insert_at_location():
    cdl = sample_list()
    try:
        cdl.insert('i',7)
        print('test_fail_insert_at_location Failed. Missing expected Exception')
    except Exception as e:
        assert 'Error' in str(e), 'Expected to rais Exception'
        print('test_fail_insert_at_location PASS. Expected Exception: "{e}"')


def test_pop():
    cdl = sample_list()
    elem = cdl.pop()
    print(cdl)
    assert elem == 'e'
    assert f"{cdl}" == "H=a ['d:a:b' -> 'a:b:c' -> 'b:c:d' -> 'c:d:a'] T=d"
    print('test_pop PASS')

def test_peek():
    cdl = sample_list()
    elem = cdl.peek()
    print(cdl)
    assert elem == 'e'
    assert f"{cdl}" == "H=a ['e:a:b' -> 'a:b:c' -> 'b:c:d' -> 'c:d:e' -> 'd:e:a'] T=e"
    print('test_peek PASS')


def test_pop_n():
    cdl = sample_list()
    elem = cdl.pop(3)
    print(cdl)
    assert elem == 'c'
    assert f"{cdl}" == "H=a ['e:a:b' -> 'a:b:d' -> 'b:d:e' -> 'd:e:a'] T=e"
    
    print('cdl pop 1')
    elem = cdl.pop(1)
    print(cdl)
    assert elem == 'a'
    assert f"{cdl}" == "H=b ['e:b:d' -> 'b:d:e' -> 'd:e:b'] T=e"
    
    print('cdl pop 3')
    elem = cdl.pop(3)
    print(cdl)
    assert elem == 'e'
    assert f"{cdl}" == "H=b ['d:b:d' -> 'b:d:b'] T=d"
    print('test_pop_n PASS')


def test_peek_n():
    cdl = sample_list()
    elem = cdl.peek(3)
    print(cdl)
    assert elem == 'c'
    elem = cdl.peek(1)
    assert elem == 'a'
    elem = cdl.peek(5)
    assert elem == 'e'
    assert f"{cdl}" == "H=a ['e:a:b' -> 'a:b:c' -> 'b:c:d' -> 'c:d:e' -> 'd:e:a'] T=e"
    print('test_peek_n PASS')

def test_fail_pop_at_location():
    try:
        cdl = sample_list()
        elem = cdl.pop(0)
        print(elem)
        print('test_fail_pop_at_location Failed. Expected Exception error')
    except Exception as e:
        assert 'Error' in str(e), 'Expected Exception Error'
        print('test_fail_pop_at_location PASS') 

def test_search():
    cdl = sample_list()
    pos = cdl.find('c')
    assert pos == 3
    pos = cdl.find('a')
    assert pos == 1
    pos = cdl.find('e')
    assert pos == 5
    pos = cdl.find('i')
    assert pos == -1
    print('test_search PASS')


def test_delete_list():
    cdl = sample_list()
    cdl.delete_all()
    assert f"{cdl}" == '[]'
    print('test_delete_list PASS')

test_create_empty_circ_double_lnkd_list()
test_insert_end_one_item_circ_double_lnkd_list()
test_insert_end_n_items_circ_double_lnkd_list()
test_iterate_circ_double_lnkd_list()
test_insert_at_location()
test_fail_insert_at_location()
test_pop()
test_peek()
test_pop_n()
test_peek_n()
test_fail_pop_at_location()
test_search()
test_delete_list()

