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

    def insert_end(self, v):
        node = SingleNode(v)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            tmp_n = self.head
            while tmp_n.next:
                tmp_n = tmp_n.next
            tmp_n.next = node
            self.tail = node

    def insert_at(self, position, value):
        index = 0
        size = 0
        node = self.head
        while node is not None and index < position -1:
            node = node.next
            if node is not None:
                size += 1
            index += 1
        if size < index:
            raise Exception("Error: position is out of bounds")
        else:
            new_node = SingleNode(value)
            if node == self.head:
                new_node.next = node
                self.head = new_node
            elif node == self.tail:
                node.next = new_node
                self.tail = new_node
            else:
                new_node.next = node.next
                node.next = new_node

    def insert_head(self, value):
        self.insert_at(0, value)

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
            return ""
        else:
            return f"H:{self.head.v} - {self.display()} - T:{self.tail.v}"



def test_create_empty_single_list():
    sl = SingleLnkdList()
    print(sl.display())
    assert sl.display() == "[]"
    print("test_create_empy_single_list Pass")

def test_insert_end_one_item_single_list():
    sl = SingleLnkdList()
    sl.insert_end('a')
    print(sl.display())
    assert sl.display() == "['a']"
    print("test_insert_end_one_item_single_list Pass")

def test_insert_end_n_items_single_list():
    sl = SingleLnkdList()
    sl.insert_end('a')
    sl.insert_end('b')
    print(sl.display())
    assert sl.display() == "['a' -> 'b']"
    assert sl.head.v == 'a'
    assert sl.tail.v == 'b'

    sl.insert_end('c')
    sl.insert_end('d')
    sl.insert_end('e')
    print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'd' -> 'e'] - T:e"
    assert sl.head.v == 'a'
    assert sl.tail.v == 'e'
    print("test_insert_end_n_items_single_list Pass")
    
def sample_test_list():
    sl = SingleLnkdList()
    sl.insert_end('a')
    sl.insert_end('b')
    sl.insert_end('c')
    sl.insert_end('d')
    sl.insert_end('e')
    return sl

def test_iterate_linked_list():
    sl = sample_test_list()
    print([node.v for node in sl])
    print("test_iterate_linked_list Pass")

def test_insert_at_location():
    sl = sample_test_list()
    sl.insert_at(3, 'f')
    print(sl.display_all())
    assert sl.display_all() == "H:a - ['a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e'] - T:e"
    sl.insert_at(0, 'g')
    print(sl.display_all())
    assert sl.display_all() == "H:g - ['g' -> 'a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e'] - T:e"
    sl.insert_at(7, 'h')
    print(sl.display_all())
    assert sl.display_all() == "H:g - ['g' -> 'a' -> 'b' -> 'c' -> 'f' -> 'd' -> 'e' -> 'h'] - T:h"
    print("test_insert_at_location Pass")

def test_fail_insert_at_location():
    sl = sample_test_list()
    try:
        sl.insert_at(6, 'a')
        print(f'test_fail_insert_at_location Fail. Missing expected Exception')
    except Exception as e:
        assert 'Error' in str(e), f'Expected to return Error'
        print(f'test_fail_insert_at_location PASS. Expected Exception: "{e}"')


def test_insert_at_head():
    sl = sample_test_list()
    sl.insert_head('i')
    print(sl.display_all())
    assert sl.display_all() == "H:i - ['i' -> 'a' -> 'b' -> 'c' -> 'd' -> 'e'] - T:e"
    print('test_insert_at_head Pass')



test_create_empty_single_list()
test_insert_end_one_item_single_list()
test_insert_end_n_items_single_list()
test_iterate_linked_list()
test_insert_at_location()
test_fail_insert_at_location()
test_insert_at_head()

# TODOs:
# test_pop() #get and delete tail
# test_peek() #return tail
# test_pop(n) #get and delete at location n
# test_peek(n) #return value at location n
# test_search(v) #return True if v exists
# test_clean() # delete all the list


