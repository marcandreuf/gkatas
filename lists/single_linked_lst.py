class SingleNode:
    def __init__(self, v=None):
        self.v = v
        self.next = None

class SingleLnkdList:
    def __init__(self):
        self.head = None
        self.tail = None

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
    

test_create_empty_single_list()
test_insert_end_one_item_single_list()
test_insert_end_n_items_single_list()

#TODO:
# test_insert_at_location_n()
# test_insert_at_head()
# test_pop() #get and delete tail
# test_peek() #return tail
# test_pop(n) #get and delete at location n
# test_peek(n) #return value at location n
# test_search(v) #return True if v exists
# test_clean() # delete all the list

