class CircQueue:
    def __init__(self, size):
        self.items = [None] * size
        self.maxSize = size
        self.start, self.top = -1, -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return f"s:{self.start} t:{self.top} {':'.join(values)}"

    def isEmpty(self):
        return self.start == -1

    def _is_full(self):
        return self.top+1 == self.start or \
            (self.start == 0 and self.top+1 == self.maxSize)
    
    def _is_empty(self):
        return self.top == -1

    def enqueue(self, value):
        if self._is_empty():
            self.start = 0
            self.top = 0
        elif self._is_full():
            raise Exception('Queue is full')
        elif self.top < self.maxSize-1:
            self.top += 1
        else:
            self.top = 0
        print(f"insert item at {self.top}")
        self.items[self.top]=value
       
    def dequeue(self):
        ret = self.items[self.start]
        self.start +=1
        return ret
        
def test_empty_circ_queue():
    cq = CircQueue(3)
    assert cq is not None
    assert cq.isEmpty()
    print("test_empty_circ_queue PASS")


def test_enqueue_to_empty():
    cq = CircQueue(3)
    cq.enqueue(1)
    assert cq.start == 0
    assert cq.top == 0
    assert cq.isEmpty() is False
    print("test_enqueue_to_empty PASS")

def test_enqueue_to_not_full():
    cq = CircQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.start == 0
    assert cq.top == 1

    cq.enqueue(3)
    assert cq.start == 0
    assert cq.top == 2
    print("test_enqueue_to_not_full PASS")

def _sample_queue():
    cq = CircQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    return cq

def test_enqueu_to_full():
    cq = _sample_queue() 
    cq.enqueue(3)
    try:
        cq.enqueue(4)
        print("test_enqueu_to_full FAIL. Expected Exception not catched")
    except Exception as e:
        assert cq.start == 0
        assert cq.top == 2
        assert "is full" in str(e), 'Expected to raise an Exception'
        print("test_enqueue_to_full PASS")


def test_dequeue_from_full():
    cq = _sample_queue()
    cq.enqueue(3)
    e = cq.dequeue()
    #print(cq)
    assert e == 1
    assert cq.start == 1
    assert cq.top == 2
    print("test_dequeue_from_full PASS")


def test_enqueue_after_full_dequeue():
    cq = _sample_queue()
    cq.enqueue(3)
    cq.dequeue()
    print(cq)
    cq.enqueue(4)
    print(cq)
    assert cq.start == 1
    assert cq.top == 0
    print("test_enqueue_after_full_dequeue PASS")



test_empty_circ_queue()
test_enqueue_to_empty()
test_enqueue_to_not_full()
test_enqueu_to_full()
test_dequeue_from_full()
test_enqueue_after_full_dequeue()
