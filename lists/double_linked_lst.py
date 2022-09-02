class DoubleNode:
    def __init__(self, v=None):
        self.v = v
        self.prev = None
        self.next = None

class DoubleLnkdList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, position=-1):
        new_node = DoubleNode(value)
        if position == -1:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                tmp = self.tail
                tmp.next = new_node
                new_node.prev = tmp
                self.tail = new_node
        elif position == 0:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
            else:
                tmp = self.head
                tmp.prev = new_node
                self.head = new_node
                new_node.next = tmp
        else:
            node = self._get_node_at_position(position)
            if node == self.tail:
                tmp = self.tail
                tmp.next = new_node
                new_node.prev = tmp
                self.tail = new_node 
            else:
                node.prev.next = new_node
                new_node.next = node
                new_node.prev = node.prev
                node.prev = new_node
            

    def _get_node_at_position(self, position):
        index = 0
        node = self.head
        while node is not self.tail and index < position-1:
            node =  node.next
            index += 1
        if position > index+2:
            raise Exception("Error: position is out of bounds")
        return node


    def display_all(self):
        if self.head == None:
            return "[]"
        else:
            return f"H={self.head.v} "+ \
                   f"{self.display()} T={self.tail.v}"

    def display(self):
        result = "["
        sep = " -> "
        node = self.head
        while node:
            prev = '-' if node.prev == None else node.prev.v
            nxt = '-' if node.next == None else node.next.v
            result += f"'{prev}:{node.v}:{nxt}'{sep}"
            node = node.next
        if len(result) > 4:
            result = result[:-4]
        return result + "]"

    
def test_create_empty_double_lnkd_list():
    dl = DoubleLnkdList()
    #print(dl.display_all())
    assert dl.display_all() == "[]"
    print('test_create_empty_double_lnkd_list Pass')

def test_insert_end_one_item_double_lnkd_list():
    dl = DoubleLnkdList()
    dl.insert('a')
    print(dl.display_all())
    assert dl.display_all() == "H=a ['-:a:-'] T=a"
    print('test_insert_end_one_item_double_lnkd_list Pass')


def test_insert_end_n_items_double_lnkd_list():
    dl = DoubleLnkdList()
    dl.insert('a')
    dl.insert('b')
    dl.insert('c')
    print(dl.display_all())
    assert dl.display_all() == "H=a ['-:a:b' -> 'a:b:c' -> 'b:c:-'] T=c"
    print('test_insert_end_n_items_double_lnkd_list Pass')


def sample_test_list():
    dl = DoubleLnkdList()
    dl.insert('a')
    dl.insert('b')
    dl.insert('c')
    dl.insert('d')
    dl.insert('e')
    return dl

def test_iterate_linked_list():
    dl = sample_test_list()
    print([node.v for node in dl])
    print('test_iterate_linked_list PASS')

def test_insert_at_location():
    dl = sample_test_list()
    print(dl.display_all())
    assert dl.display_all() == "H=a ['-:a:b' -> 'a:b:c' -> 'b:c:d' -> 'c:d:e' -> 'd:e:-'] T=e"
    dl.insert('f', 3)
    print(dl.display_all())
    assert dl.display_all() == "H=a ['-:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:-'] T=e"
    dl.insert('g', 0)
    print(dl.display_all())
    assert dl.display_all() == "H=g ['-:g:a' -> 'g:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:-'] T=e"
    dl.insert('h', 8)
    print(dl.display_all())
    assert dl.display_all() == "H=g ['-:g:a' -> 'g:a:b' -> 'a:b:f' -> 'b:f:c' -> 'f:c:d' -> 'c:d:e' -> 'd:e:h' -> 'e:h:-'] T=h"
    print('test_insert_at_location PASS')
    

#def test_fail_insert_at_location():
#    dl = sample_test_list()
#    try:
#        dl.insert(
#

test_create_empty_double_lnkd_list()
test_insert_end_one_item_double_lnkd_list()
test_insert_end_n_items_double_lnkd_list()
test_iterate_linked_list()
test_insert_at_location()
#test_fail_insert_at_location()
#test_pop()
#test_peek()
#test_pop_n()
#test_peek_n()
#test_fail_pop_at_location()
#test_search()
#test_delete_list()

