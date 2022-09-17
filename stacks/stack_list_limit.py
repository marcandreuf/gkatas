
class StackListLimit():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return f"[{':'.join(values)}] max={self.maxSize}"

    def __len__(self):
        return len(self.list)

    def max(self):
        return self.maxSize

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is full")
        else:
            self.list.append(value)
    
    def isFull(self):
        return False if len(self.list) < self.maxSize else True

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()

    def peek(self):
        return self.list[-1]

    def delete(self):
        self.list.clear()

def test_empty_list():
    s = StackListLimit(3)
    assert s.max() == 3
    assert len(s) == 0
    assert s.isEmpty()
    print(s)
    assert f"{s}" == "[] max=3"
    print("test_empty_list PASS")


def test_push_stack():
    s = StackListLimit(3)
    s.push(1)
    assert f"{s}" == "[1] max=3"
    s.push(2)
    assert f"{s}" == "[2:1] max=3"
    s.push(3)
    assert f"{s}" == "[3:2:1] max=3"

    try:
        s.push(4)
        raise Exception('Not possible to push after max size')
    except Exception as e:
        assert "is full" in str(e), 'Expected is full exception'
    assert f"{s}" == "[3:2:1] max=3"    

    print("test_push_stack PASS")

def test_is_full_stack():
    s = StackListLimit(3)
    s.push(1)
    assert s.isFull() == False
    s.push(2)
    s.push(3)
    assert s.isFull() == True

def test_pop_stack():
    s = StackListLimit(3)
    s.push(1)
    s.push(2)
    p1 = s.pop()
    assert p1 == 2
    assert f"{s}" == "[1] max=3"
    p2 = s.pop()
    assert p2 == 1
    p3 = s.pop()
    assert p3 == None
    print("test_pop_stack PASS")

def test_peek_stack():
    s = StackListLimit(3)
    s.push(1)
    s.push(2)
    assert f"{s}" == "[2:1] max=3"
    p1 = s.peek()
    assert f"{s}" == "[2:1] max=3"
    print("test_peek_stack PASS")
 
def test_delete_stack():
    s = StackListLimit(3)
    s.push(1)
    s.push(2)
    assert f"{s}" == "[2:1] max=3"
    s.delete()
    assert f"{s}" == "[] max=3"
    print("test_delete_stack PASS")

test_empty_list()
test_push_stack()
test_is_full_stack()
test_pop_stack()
test_peek_stack()
test_delete_stack()
