class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        str_prev = self._format_str_node_value(self.prev)
        str_next = self._format_str_node_value(self.next)
        return f"'{str_prev}:{str(self.value)}:{str_next}'"

    def _format_str_node_value(self, node):
        return "-" if node is None else str(node.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return self._print_do_while_loop()

    def _print_do_while_loop(self):
        ret = "["
        node = self.head
        while True:
            ret += f"{str(node)}"
            if node.next is self.head:
                break
            else:
                node = node.next
        return f"{ret}]"

    def _print_while_loop(self):
        node = self.head
        ret = f"[{str(node)}"
        node = node.next
        while node is not None and node is not self.head:        
            ret += f", {str(node)}"
            node = node.next
        return f"{ret}]"



    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tmp = self.tail
            tmp.next = new_node
            self.tail = new_node
            new_node.prev = tmp
            new_node.next = self.head

            
def test_insert():
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    print(ll)

test_insert()


