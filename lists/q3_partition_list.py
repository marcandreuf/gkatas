# Write code to partition a linked list around a value x, such that all nodes less than x come before al lnodes grater than or equal to x.

from linked_list import LinkedList


def partition_list(ll, x):
    ret = LinkedList()
    if ll.head == None:
        return ret
    else:
        ret.add(ll.head.value)
        n = ll.head.next
        while n:
            if n.value < x:                
                ret.add_head(n.value)
            else:
                ret.add(n.value)
            n = n.next
        return ret

def test_part_empty_list():
    ll = LinkedList()
    assert f"{partition_list(ll, 50)}" == "[]"
    print("test_part_empty_list PASS")
    
def test_part_one_item_list():
    items = [1]
    ll = LinkedList(items)
    pl = partition_list(ll, 50)
    #print(pl)
    assert f"{pl}" == "[1]"
    print("test_part_one_item_list PASS")

def test_part_two_items_list():
    items = [3,1]
    ll = LinkedList(items)
    #print(ll)
    pl = partition_list(ll, 2)
    #print(pl)
    assert f"{pl}" == "[1 -> 3]"
    print("test_part_two_items_list PASS")


def test_partition_list():
    items = [89, 48, 36, 93, 14, 69, 33, 68, 67, 45]
    ll = LinkedList(items)
    print(ll)
    plist = partition_list(ll, 50)
    print(f"{plist} on x=50")
    assert f"{plist}" == "[45 -> 33 -> 14 -> 36 -> 48 -> 89 -> 93 -> 69 -> 68 -> 67]"
    print("test_partition_list PASS")

test_part_empty_list()
test_part_one_item_list()
test_part_two_items_list()
test_partition_list()

