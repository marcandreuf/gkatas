class MultiStack:
    def __init__(self, stack_size = 0, stacks_num = 0):
        self.list = [0] * (stack_size * stacks_num)
        self.tops = [0] * stacks_num
        self.stacks_num = stacks_num
        self.stack_size = stack_size

    def __str__(self):
        vals = [str(x) for x in self.list]
        tops = [str(y) for y in self.tops]
        return f"[{','.join(vals)}] - {':'.join(tops)}"

    def stacks(self):
        return self.stacks_num

    def isEmptyStack(self, stack):
        return self.tops[stack] == 0

    def _index_top_n(self, stack_num):
        offset = self.stack_size * stack_num
        return offset + self.tops[stack_num]

    def push(self, value, stack_num):
        if self.tops[stack_num] >= self.stack_size:
            raise Exception(f"Error stack {stack_num} is full")
        index = self._index_top_n(stack_num)
        self.list[index] = value
        self.tops[stack_num] += 1
    
    def pop(self, stack_num):
        if self.isEmptyStack(stack_num):
            return None
        index = self._index_top_n(stack_num)
        ret = self.list[index-1]
        self.list[index-1] = 0
        self.tops[stack_num] -= 1
        return ret


def test_create_multistack():
    ms = MultiStack(3, 3)
    assert ms.stacks() == 3
    assert ms.isEmptyStack(0)
    assert ms.isEmptyStack(1)
    assert ms.isEmptyStack(2)
    print("test_create_multistack PASS")


def test_push_into_stack_n():
    ms = MultiStack(3, 3)
    ms.push(1, 0)
    print(ms)
    assert f"{ms}" == "[1,0,0,0,0,0,0,0,0] - 1:0:0"
    assert ms.isEmptyStack(0) is False
    assert ms.isEmptyStack(1)
    assert ms.isEmptyStack(2)
    
    ms.push(1, 1)
    print(ms)
    assert f"{ms}" == "[1,0,0,1,0,0,0,0,0] - 1:1:0"
    assert ms.isEmptyStack(0) is False
    assert ms.isEmptyStack(1) is False
    assert ms.isEmptyStack(2)
    
    ms.push(1, 2)
    print(ms)
    assert f"{ms}" == "[1,0,0,1,0,0,1,0,0] - 1:1:1"
    assert ms.isEmptyStack(0) is False
    assert ms.isEmptyStack(1) is False
    assert ms.isEmptyStack(2) is False

    print("test_push_into_stack_n PASS")


def test_stack_one_is_full():
    ms = MultiStack(3, 3)
    ms.push(1, 0)
    ms.push(1, 0)
    ms.push(1, 0)
    print(ms)
    assert f"{ms}" == "[1,1,1,0,0,0,0,0,0] - 3:0:0"
    
    try:
        ms.push(1, 0)
        print("test_stack_one_is_full FAIL, expected a full stack exception")
    except Exception as e:
        assert "stack 0 is full" in str(e)
        assert f"{ms}" == "[1,1,1,0,0,0,0,0,0] - 3:0:0"
        print("test_stack_one_is_full PASS")

def test_stack_three_is_full():
    ms = MultiStack(3, 3)
    ms.push(1, 2)
    ms.push(1, 2)
    ms.push(1, 2)
    print(ms)
    assert f"{ms}" == "[0,0,0,0,0,0,1,1,1] - 0:0:3"
    
    try:
        ms.push(1, 2)
        print("test_stack_three_is_full FAIL, expected a full stack exception")
    except Exception as e:
        assert "stack 2 is full" in str(e)
        assert f"{ms}" == "[0,0,0,0,0,0,1,1,1] - 0:0:3"
        print("test_stack_three_is_full PASS")


def test_print_stack_n():
    ms = MultiStack(3, 3)
    assert f"{ms}" == "[0,0,0,0,0,0,0,0,0] - 0:0:0" 
    

def test_pop_stack_n():
    ms = MultiStack(3, 3)
    ms.push(1, 2)
    ms.push(2, 2)
    ms.push(3, 2)
    print(ms)
    assert f"{ms}" == "[0,0,0,0,0,0,1,2,3] - 0:0:3"
    e = ms.pop(2)
    print(e)
    assert e == 3
    print(ms)
    assert f"{ms}" == "[0,0,0,0,0,0,1,2,0] - 0:0:2"

    e = ms.pop(2)
    print(e)
    assert e == 2
    print(ms)
    assert f"{ms}" == "[0,0,0,0,0,0,1,0,0] - 0:0:1"

    e = ms.pop(2)
    print(e)
    assert e == 1
    print(ms)
    assert f"{ms}" == "[0,0,0,0,0,0,0,0,0] - 0:0:0"

    e = ms.pop(2)
    assert e == None
    assert f"{ms}" == "[0,0,0,0,0,0,0,0,0] - 0:0:0"
    assert ms.isEmptyStack(0) is True
    assert ms.isEmptyStack(1) is True
    assert ms.isEmptyStack(2) is True

    print("test_pop_stack_n PASS")


    

test_create_multistack()
test_push_into_stack_n()
test_stack_one_is_full()
test_stack_three_is_full()
test_print_stack_n()
test_pop_stack_n()



