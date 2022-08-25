class SingleNode:
    def __init__(self, v=None):
        self.v = v
        self.next = None

class CircSingleLnkdList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display_all(self):
        if self.head == None:
            return '[]'


def test_create_empty_circ_single_list():
    sl = CircSingleLnkdList()
    #print(sl.display_all())
    assert sl.display_all() == '[]'
    print('test_create_empty_circ_single_list Pass')

test_create_empty_circ_single_list()
#test_insert_end_one_item_single_list()
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
#
