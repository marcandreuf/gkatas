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


    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


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
    print('test_generate PASS')
    

if __name__ == "__main__":
    test_generate()
    test_add()



