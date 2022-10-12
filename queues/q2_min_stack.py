# Proof of concept
class Node:
    def __init__(self, value, min_value):
        self.value = value
        self.min = min_value
        self.next = None

    def __str__(self):
        val = str(self.value)
        if self.next:
            val += ','+str(self.next)
        return val

class MinStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def min(self):
        return self.head.min if self.head else None

    def push(self, value):
        if self.head is None:
            self.head = Node(value, value)            
        else:
            stack_min = self.head.min if self.head.min < value else value
            new_node = Node(value, stack_min)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            ret = self.head.value
            self.head = self.head.next
            return ret


def test_create_min_stack():
    s = MinStack()
    assert s.isEmpty()
    print("test_create_min_stack PASS")

def test_push_min():
    s = MinStack()
    s.push(5)
    assert s.min() == 5
    s.push(6)
    assert s.min() == 5
    s.push(3)
    assert s.min() == 3
    s.push(1)
    assert s.min() == 1
    print("test_push_min PASS")

def test_pop_min():
    s = MinStack()
    s.push(5)
    s.push(6)
    s.push(3)
    s.push(1)
    assert s.min() == 1
    e = s.pop()
    assert e == 1
    assert s.min() == 3
    e = s.pop()
    assert e == 3
    assert s.min() == 5
    print("test_pop_min PASS")

test_create_min_stack()
test_push_min()
test_pop_min()
