# Proof of concept
# TODO implement all tests and refactor the code

class Node:
    def __init__(self, value, min_value):
        self.value = value
        self.min = min_value
        self.next = None

    def __str__(self):
        val = str(self.value)
        if self.next:
            val += ','+str(self.next)
        return val

class MinStack:
    def __init__(self):
        self.head = None

    def min(self):
        return self.head.min if self.head else None

    def push(self, value):
        if self.head is None:
            self.head = Node(value, value)            
        else:
            stack_min = self.head.min if self.head.min < value else value
            new_node = Node(value, stack_min)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            ret = self.head.value
            self.head = self.head.next
            return ret


s = MinStack()
s.push(5)
print(s.head)
print(s.min())
print("---")
s.push(6)
print(s.head)
print(s.min())
print("---")
s.push(3)
print(s.head)
print(s.min())
print("---")
e = s.pop()
print(e)
print(s.head)
print(s.min())
            


