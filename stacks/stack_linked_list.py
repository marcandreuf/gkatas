from lists.linked_list import LinkedList


class StackLinkedList():
    def __init__(self):
        self.llist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.llist]
        return f"[{' : '.join(values)}]"
   
def test_empty_llist_stack():
    s = StackLinkedList()
    print(s)
   # assert f"{s}" == "[]"
   # print("test_empty_llist_stack PASS")

test_empty_llist_stack()

