class CircQueue:
    def __init__(self, size):
        self.items = [None] * size
        self.maxSize = size
        self.start, self.top = None, None

    def __str__(self):
        values = [str(x) for x in self.items]
        return f"s:{self.start} t:{self.top} {':'.join(values)}"

    def isEmpty(self):
        return self.top == None

    def isFull(self):
        return self.top+1 == self.start or \
            (self.start == 0 and self.top+1 == self.maxSize)

    def enqueue(self, value):
        if self.isEmpty():
            self.start = 0
            self.top = 0
        elif self.isFull():
            raise Exception('Queue is full')
        elif self.top+1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
        #print(f"insert item at {self.top}")
        self.items[self.top]=value
       
    def dequeue(self):
        if self.start == None:
            return None
        start = self.start
        ret = self.items[self.start]
        if self.start+1 == self.maxSize:
            self.start = 0
        elif self.start == self.top:
            self.start = None
            self.top = None
        else:
            self.start +=1
        self.items[start] = None
        return ret

    def peek(self):
        return self.items[self.start]

    def delete(self):
        #for i in range(self.maxSize):
        #    self.items[i] = None
        self.items = [None] * self.maxSize
        self.start = None
        self.top = None
        
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


def test_enqueue_after_dequeue_from_full():
    cq = _sample_queue()
    cq.enqueue(3)
    e = cq.dequeue()
    #print(cq)
    assert e == 1
    cq.enqueue(4)
    #print(cq)
    assert cq.start == 1
    assert cq.top == 0
    
    e = cq.dequeue()
    assert e == 2
    cq.enqueue(5)
    #print(cq)
    assert cq.start == 2
    assert cq.top == 1

    e = cq.dequeue()
    assert e == 3
    cq.enqueue(6)
    #print(cq)
    assert cq.start == 0
    assert cq.top == 2
    print("test_enqueue_after_dequeue_from_full PASS")

def test_dequeu_from_empty():
    cq = CircQueue(3)
    e = cq.dequeue()
    #print(cq)
    #print(e)
    assert e == None
    print("test_dequeu_from_empty PASS")

def test_dequeu_last_itme():
    cq = CircQueue(3)
    cq.enqueue(1)
    e = cq.dequeue()
    #print(cq)
    assert e == 1
    assert cq.start == None
    assert cq.top == None
    assert f"{cq}" == "s:None t:None None:None:None"
    print("test_dequeu_last_itme PASS")

def test_peek():
    cq = _sample_queue()
    e = cq.peek()
    assert e == 1
    assert f"{cq}" == "s:0 t:1 1:2:None"
    print("test_peek PASS")

def test_delete():
    cq = _sample_queue()
    cq.enqueue(4)
    assert f"{cq}" == "s:0 t:2 1:2:4"
    cq.delete()
    #print(cq)
    assert f"{cq}" == "s:None t:None None:None:None"
    print("test_delete PASS")

test_empty_circ_queue()
test_enqueue_to_empty()
test_enqueue_to_not_full()
test_enqueu_to_full()
test_dequeue_from_full()
test_enqueue_after_dequeue_from_full()
test_dequeu_from_empty()
test_dequeu_last_itme()
test_peek()
test_delete()
