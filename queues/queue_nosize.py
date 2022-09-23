class QueueNoSize:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return f"[{':'.join(values)}]"

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def delete(self):
        self.items = []

def test_empty_queue():
    q = QueueNoSize()
    assert q.isEmpty()
    assert f"{q}" == "[]"
    print("test_empty_queue PASS")

def test_enqueue():
    q = QueueNoSize()
    q.enqueue(1)
    assert q.isEmpty() == False
    assert f"{q}" == "[1]"
    
    q.enqueue(2)
    assert f"{q}" == "[1:2]"
    print("test_enqueue PASS")
    
def _sample_queue():
    q = QueueNoSize()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    return q

def test_dequeue():
    q = _sample_queue()
    assert f"{q}" == "[1:2:3:4]"
    e = q.dequeue()
    assert e == 1
    assert f"{q}" == "[2:3:4]"
    print("test_dequeue PASS")


def test_peek():
    q = _sample_queue() 
    assert f"{q}" == "[1:2:3:4]"
    e = q.peek()
    assert e == 1
    assert f"{q}" == "[1:2:3:4]"
    print("test_peek PASS")


def test_delete():
    q = _sample_queue() 
    q.delete()
    assert q.isEmpty()
    print("test_delete PASS")


test_empty_queue()
test_enqueue()
test_dequeue()
test_peek()
test_delete()


