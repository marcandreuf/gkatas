from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            for v in values:
                self.add(v)

    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return f"[{' -> '.join(values)}]"

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self.tail

    def add_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def join(self, ll):
        self.tail.next = ll.head
        self.tail = ll.tail
        return self

    def pop_head(self):
        if self.head is None:
            return None
        ret = self.head.value
        self.head = self.head.next
        return ret


def test_generate():
    ll = LinkedList().generate(5, 10, 20)
    print(ll)
    assert len(ll) == 5
    print('test_generate PASS')

def test_add():
    ll = LinkedList()
    ll.generate(5, 10, 20)
    print(ll)
    assert len(ll) == 5
    ll.add(6)
    print(ll)
    assert len(ll) == 6
    print('test_add PASS')
    

def test_add_head():
    ll = LinkedList()
    ll.generate(3, 10, 20)
    print(ll)
    assert ll.head != 50
    ll.add_head(50)
    print(ll)    
    assert ll.head.value == 50
    print("test_add_head PASS")


def test_join_lists():
    l1 = LinkedList([1,2,3])
    l2 = LinkedList([4,5,6])
    l3 = l1.join(l2)
    assert f"{l3}" == "[1 -> 2 -> 3 -> 4 -> 5 -> 6]"
    n = l3.head
    for i in range(3):
        n = n.next
    assert l2.head is n
    assert l3.head is l1.head 
    assert l3.tail is l2.tail
    print("test_join_lists PASS")

def test_pop_head():
    l1 = LinkedList([1,2,3])
    e = l1.pop_head()
    assert e == 1
    assert l1.tail.value == 3
    assert l1.head.value == 2
    l2 = LinkedList()
    e = l2.pop_head()
    assert e is None
    print("test_pop_head PASS")


if __name__ == "__main__":
    test_generate()
    test_add()
    test_add_head()
    test_join_lists()
    test_pop_head()

