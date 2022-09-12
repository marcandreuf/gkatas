
from linked_list import LinkedList

def nth_to_last(lst, n):
    node = lst.head
    for i in range(n):
        if node == None:
            return -1
        p1 = node
        node = node.next
    p2 = lst.head
    while p1 is not lst.tail:
        p2 = p2.next
        p1 = p1.next
    return p2.value


def test_nth_to_last():
    items = [89, 48, 36, 93, 14, 69, 33, 68, 67, 45]
    ll = LinkedList(items)
    print(ll)
    assert nth_to_last(ll, 3) == 68
    
    items = []
    ll = LinkedList(items)
    print(ll)
    assert nth_to_last(ll, 3) == -1

    items = [1,3]
    ll = LinkedList(items)
    print(ll)
    assert nth_to_last(ll, 1) == 3
  
    print('test_nth_to_last PASS')


test_nth_to_last()

