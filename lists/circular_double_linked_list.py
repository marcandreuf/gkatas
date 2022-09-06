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
        
    def _get_node_at_position(self, position):
        index = 0
        node = self.head
        while node is not self.tail and index < position-1:
            node = node.next
            index += 1
        if position > index+2:
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



test_create_empty_circ_double_lnkd_list()
test_insert_end_one_item_circ_double_lnkd_list()
test_insert_end_n_items_circ_double_lnkd_list()
test_iterate_circ_double_lnkd_list()
test_insert_at_location()
test_fail_insert_at_location()
#test_pop()
#test_peek()
#test_pop_n()
#test_peek_n()
#test_fail_pop_at_location()
#test_search()
#test_delete_list()
#
