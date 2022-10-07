class MultiStack:
    def __init__(self, stack_size = 0, stacks_num = 0):
        self.list = [0] * (stack_size * stacks_num)
        self.stacks_top = [0] * stacks_num
        self.stacks_num = stacks_num
        self.stack_size = stack_size

    def stacks(self):
        return self.stacks_num

    def isEmptyStack(self, stack):
        return self.stacks_top[stack-1] == 0
        


def test_create_multistack():
    ms = MultiStack(3, 3)
    assert ms.stacks() == 3
    assert ms.isEmptyStack(1)
    assert ms.isEmptyStack(2)
    assert ms.isEmptyStack(3)
    print("test_create_multistack PASS")



test_create_multistack()



