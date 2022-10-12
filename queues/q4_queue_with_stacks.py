class QueueStacks:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def __str__(self):
        return f"<s1{str(self.stk1)}:s2{str(self.stk2)}>"

    def isEmpty(self):
        return len(self.stk1) == 0
        
    def push(self, value):
        self.stk1.append(value)

    def pop(self):
        if len(self.stk1) == 0:
            return 0
        else:
            while len(self.stk1) > 0:
                self.stk2.append(self.stk1.pop())
            ret = self.stk2.pop()
            while len(self.stk2) > 0:
                self.stk1.append(self.stk2.pop())
            return ret

def test_create_empty_queue():
    qs = QueueStacks()
    assert qs.isEmpty()
    print(qs)
    assert f"{qs}" == "<s1[]:s2[]>"
    print("test_create_empty_queue PASS")

def test_push():
    qs = QueueStacks()
    qs.push(1)
    qs.push(2)
    assert qs.isEmpty() == False
    print(qs)
    assert f"{qs}" == "<s1[1, 2]:s2[]>"
    print("test_push PASS")


def test_pop():
    qs = QueueStacks()
    qs.push(1)
    qs.push(2)
    qs.push(3)
    assert f"{qs}" == "<s1[1, 2, 3]:s2[]>"
    e = qs.pop()
    assert e == 1
    print(qs)
    assert f"{qs}" == "<s1[2, 3]:s2[]>"
    e = qs.pop()
    assert e == 2
    print(qs)
    assert f"{qs}" == "<s1[3]:s2[]>"
    e = qs.pop()
    assert e == 3
    print(qs)
    assert f"{qs}" == "<s1[]:s2[]>"
    assert qs.isEmpty()

    print("test_pop PASS")

test_create_empty_queue()
test_push()
test_pop()



