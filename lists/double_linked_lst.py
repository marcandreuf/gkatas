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

    def insert(self, value):
        new_node = DoubleNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

    def display_all(self):
        if self.head == None:
            return "[]"
        else:
            return f"H:{self.head.v} - H.prev:{self.head.prev} "+ \
                   f"- {self.display()} - T:{self.tail.v} - "+ \
                   f"T.next:{self.tail.next}"

    def display(self):
        result = "["
        sep = " -> "
        node = self.head
        while node:
            result += f"'{node.v}'{sep}"
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
    assert dl.display_all() == "H:a - H.prev:None - "+ \
                               "['a'] - "+ \
                               "T:a - T.next:None"
    print('test_insert_end_one_item_double_lnkd_list Pass')


test_create_empty_double_lnkd_list()
test_insert_end_one_item_double_lnkd_list()
#test_insert_end_n_items_single_list()
#test_iterate_linked_list()
#test_insert_at_location()
#test_fail_insert_at_location()
#test_pop()
#test_peek()
#test_pop_n()
#test_peek_n()
#test_fail_pop_at_location()
#test_search()
#test_delete_list()

