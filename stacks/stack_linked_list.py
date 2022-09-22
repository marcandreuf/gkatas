from lists.linked_list import LinkedList


class StackLinkedList():
    def __init__(self):
        self.llist = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.llist]
        return f"[{' : '.join(values)}]"

    def isEmpty(self):
        return len(self.llist) == 0

    def push(self, value):
        self.llist.add_head(value)

    def pop(self):
        return self.llist.pop_head()

    def peek(self):
        return self.llist.head.value
   
def test_empty_llist_stack():
    s = StackLinkedList()
    print(s)
    assert s.isEmpty()
    assert f"{s}" == "[]"
    print("test_empty_llist_stack PASS")

def test_push_llist_stack():
    s = StackLinkedList()
    s.push('a')
    print(s)
    assert s.isEmpty() == False
    assert f"{s}" == "[a]"
    s.push('b')
    print(s)
    assert f"{s}" == "[b : a]"

def _sample_stack():
    s = StackLinkedList()
    s.push(1)
    s.push(2)
    s.push(3)
    return s

def test_pop_llist_stack():
    s = _sample_stack()
    print(s)
    assert f"{s}" == "[3 : 2 : 1]"
    e = s.pop()
    assert e == 3
    assert f"{s}" == "[2 : 1]"
    print("test_pop_llist_stack PASS")

def test_pop_empty_stack():
    s = StackLinkedList()
    e = s.pop()
    assert e is None
    print("test_pop_empty_stack PASS")

def test_peek_llist_stack():
    s = _sample_stack()
    assert f"{s}" == "[3 : 2 : 1]"
    e = s.peek()
    assert e == 3
    assert f"{s}" == "[3 : 2 : 1]"


test_empty_llist_stack()
test_push_llist_stack()
test_pop_llist_stack()
test_pop_empty_stack()
test_peek_llist_stack()

