
class Stack:
    def __init__(self, values=[]):
        self.list = []
        if values != []:
            for v in values:
                self.push(v)

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return f"[{':'.join(values)}]"

    def isEmpty(self):
        return True if len(self.list) == 0 else False
    
    def push(self, value):
        self.list.append(value)
       
    def pop(self):
        #return self.list.pop() if len(self.list)>0 else None
        if len(self.list) > 0:
            r = self.list[-1]
            del self.list[-1]
            return r
        return None

    def peek(self):
        return self.list[-1] if len(self.list) > 0 else None

    def delete(self):
        self.list.clear()

def test_empty_stack():
    s = Stack()
    #print(s)
    assert s.isEmpty()
    print("test_empty_stack PASS")

def test_init_stack():
    s = Stack([1,2,3])
    #print(s)
    assert f"{s}" == "[3:2:1]"
    print("test_init_stack PASS")

def test_push_stack():
    s = Stack()
    s.push(1)
    #print(s)
    assert f"{s}" == "[1]"
    s.push(2)
    #print(s)
    assert f"{s}" == "[2:1]"
    print("test_push_stack PASS")

def test_pop_stack():
    s = Stack([1,2,3])
    p1 = s.pop()
    assert p1 == 3
    assert f"{s}" == "[2:1]"

    p2 = s.pop()
    assert p2 == 2
    assert f"{s}" == "[1]"

    p3 = s.pop()
    assert p3 == 1    
    assert f"{s}" == "[]"

    p4 = s.pop()
    assert p4 == None
    print("test_pop_stack PASS")

def test_peek_stack():
    s = Stack([1,2,3])
    p1 = s.peek()
    assert p1 == 3
    assert f"{s}" == "[3:2:1]"

    s = Stack()
    p = s.peek()
    assert p == None
    
    print("test_peek_stack PASS")

def test_delete_stack():
    s = Stack([1,2,3])
    assert f"{s}" == "[3:2:1]"
    s.delete()
    assert f"{s}" == "[]"
    print("test_delete_stack PASS")


test_empty_stack()
test_init_stack()
test_push_stack()
test_pop_stack()
test_peek_stack()
test_delete_stack()
