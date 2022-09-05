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
    
    def insert(self, value):
        new_node = DoubleNode(value)
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



    def display_all(self):
        if self.head == None:
            return '[]'
        else:
            return f"H={self.head.v} {self.display()} T={self.tail.v}"
        

    def display(self):
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
    #print(cdl.display_all())
    assert cdl.display_all() == '[]'
    print('test_create_empty_circ_double_lnkd_list PASS')


def test_insert_end_one_item_circ_double_lnkd_list():
    cdl = CircDoubleLnkdList()
    cdl.insert('a')
    print(cdl.display_all())
    assert cdl.display_all() == "H=a ['a:a:a'] T=a"
    print('test_insert_end_one_item_double_lnkd_list PASS')
    

def test_insert_end_n_items_circ_double_lnkd_list():
    cdl = CircDoubleLnkdList()
    cdl.insert('a')
    cdl.insert('b')
    cdl.insert('c')
    print(cdl.display_all())
    assert cdl.display_all() == "H=a ['c:a:b' -> 'a:b:c' -> 'b:c:a'] T=c"
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

    


test_create_empty_circ_double_lnkd_list()
test_insert_end_one_item_circ_double_lnkd_list()
test_insert_end_n_items_circ_double_lnkd_list()
test_iterate_circ_double_lnkd_list()
#test_insert_at_location()
#test_fail_insert_at_location()
#test_pop()
#test_peek()
#test_pop_n()
#test_peek_n()
#test_fail_pop_at_location()
#test_search()
#test_delete_list()
#
