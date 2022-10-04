
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    
    def __str__(self):
        values = [str(x) for x in self]
        return f"[{':'.join(values)}]"


class QueueLinkList:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return str(self.ll)

    def enqueue(self, value):
        newNode = Node(value)
        if self.ll.head == None:
            self.ll.head = newNode
            self.ll.tail = newNode
        else:
            self.ll.tail.next = newNode
            self.ll.tail = newNode

def test_empty_queue():
    q = QueueLinkList()
    print(q)
    assert q.ll.head == None
    print("test_empty_queue PASS")

def test_enqueue():
    q = QueueLinkList()
    q.enqueue(1)
    print(q)
    assert q.ll.head != None
    assert f"{q}" == "[1]"
    
    q.enqueue(2)
    print(q)
    assert f"{q}" == "[1:2]"

    q.enqueue(3)
    print(q)
    assert f"{q}" == "[1:2:3]"
    
    print("test_enqueue PASS")

test_empty_queue()
test_enqueue()
