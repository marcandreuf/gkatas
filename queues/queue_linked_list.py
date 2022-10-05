
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

    def isEmpty(self):
        return True if self.ll.head == None else False

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            ret = self.ll.head.value
            self.ll.head = self.ll.head.next
            return ret

    def delete(self):
        self.ll.head = None
        self.ll.tail = None

def test_empty_queue():
    q = QueueLinkList()
    assert q.ll.head == None
    assert q.isEmpty(), 'Expecting to be empty queue'
    print("test_empty_queue PASS")

def test_enqueue():
    q = QueueLinkList()
    q.enqueue(1)
    assert q.ll.head != None
    assert f"{q}" == "[1]"
    q.enqueue(2)
    assert f"{q}" == "[1:2]"
    q.enqueue(3)
    assert f"{q}" == "[1:2:3]"
    print("test_enqueue PASS")


def test_dequeue():
    q = QueueLinkList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert f"{q}" == "[1:2:3]"
    e = q.dequeue()
    assert e == 1
    assert f"{q}" == "[2:3]"
    q.dequeue()
    q.dequeue()
    e = q.dequeue()
    assert e == None
    print("test_dequeue PASS")

def test_delete():
    q = QueueLinkList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.delete()
    assert q.isEmpty()
    print("test_delete PASS")

test_empty_queue()
test_enqueue()
test_dequeue()
test_delete()
