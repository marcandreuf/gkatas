class SingleNode:
    def __init__(self, v=None):
        self.v = v
        self.next = None

class CircSingleLnkdList:
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
        new_node = SingleNode(value)
        if position == -1:
            if self.head == None:
                self.head = new_node
                self.tail = new_node
                self.tail.next = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        else:
            node = self._get_node_at_position(position)
            if node == self.tail:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = node.next
                node.next = new_node
            
    
    def _get_node_at_position(self, position):
        if position == 0:
            return self.head
        index = 1
        node = self.head.next
        while index < position-1:
            if node == self.head:
                raise Exception("Error: index out of bounds")
            node = node.next
            index += 1
        return node
   


    def display_all(self):
        if self.head == None:
            return '[]'
        else:
            return f"H:{self.head.v} - "\
                    +f"{self._display()} - "\
                    +f"T:{self.tail.v} - "\
                    +f"T-next:{self.tail.next.v}"

    def _display(self):
        sep = ' -> '
        suf = ']'
        result = f"['{self.head.v}'{sep}"
        node = self.head.next
        while node and node != self.head:
            result += f"'{node.v}'{sep}"
            node = node.next
        return result[:-4] + suf

def test_create_empty_circ_single_list():
    sl = CircSingleLnkdList()
    #print(sl.display_all())
    assert sl.display_all() == '[]'
    print('test_create_empty_circ_single_list Pass')

def test_insert_at_end_circ_single_list():
    sl = CircSingleLnkdList()
    sl.insert('a')
    print(sl.display_all())
    assert sl.display_all() == "H:a - ['a'] - T:a - T-next:a"
    print('test_insert_at_end_circ_single_list Pass')


def test_insert_at_end_n_items_circ_single_list():
    sl = sample_test_list()
    print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'd' -> 'e'] - T:e - T-next:a"
    print('test_insert_at_end_n_items_circ_single_list Pass')

def sample_test_list():
    sl = CircSingleLnkdList()
    sl.insert('a')
    sl.insert('b')
    sl.insert('c')
    sl.insert('d')
    sl.insert('e')
    return sl

def test_iterate_circ_single_list():
    sl = sample_test_list()
    print([node.v for node in sl])
    print("test_iterate_linked_list Pass")

def test_insert_at_location():
    sl = sample_test_list()
    sl.insert('f', 3)
    #print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e'] - T:e - T-next:a"
    sl.insert('g',6)
    #print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e' -> 'g'] - T:g - T-next:a"
    print('test_insert_at_location Pass')

def test_fail_insert_at_location():
    sl = sample_test_list()
    try:
        sl.insert('z', 10)
        print('test_fail_insert_at_location Fial. Missing expected Exception')
    except Exception as e:
        assert 'Error' in str(e), f'Excpected to return Error'
        print(f'test_fail_insert_at_location PASS. Expected Exception: "{e}"')


test_create_empty_circ_single_list()
test_insert_at_end_circ_single_list()
test_insert_at_end_n_items_circ_single_list()
test_iterate_circ_single_list()
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
