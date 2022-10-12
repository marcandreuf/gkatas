class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        ret = "<"
        for s in self.stacks:
            ret += str(s) + ":"
        return ret[:-1] + ">"

    def isEmpty(self):
        return len(self.stacks) == 0
   
    def push(self, value):
        if self.isEmpty():
            self.stacks.append([value])
        else:
            if len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].append(value)
            else:
                self.stacks.append([value])
    
    def pop(self):
        if len(self.stacks) == 0:
            return None
        else:
            ret = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            return ret



def test_create_plate_stack():
    ps = PlateStack(3)
    print(ps)
    assert ps.isEmpty()
    print("test_create_plate_stack PASS")

def test_push():
    ps = PlateStack(2)
    ps.push(1)
    print(ps)
    assert ps.isEmpty() == False
    assert f"{ps}" == "<[1]>"

    ps.push(2)
    print(ps)
    assert f"{ps}" == "<[1, 2]>"

    ps.push(3)
    print(ps)
    assert f"{ps}" == "<[1, 2]:[3]>"

    ps.push(4)
    print(ps)
    assert f"{ps}" == "<[1, 2]:[3, 4]>"

    print("test_push PASS")

def test_pop():
    ps = PlateStack(2)
    ps.push(1)
    ps.push(2)
    ps.push(3)
    print(ps)
    assert f"{ps}" == "<[1, 2]:[3]>"
    e = ps.pop()
    print(ps)
    assert e == 3
    assert f"{ps}" == "<[1, 2]>"
    e = ps.pop()
    print(ps)
    assert e == 2
    assert f"{ps}" == "<[1]>"

    print("test_pop PASS")


test_create_plate_stack()
test_push()
test_pop()



