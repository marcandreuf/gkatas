"""
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the fist linked list is the exact same node (by reference) as the jth node of second linked list, then they are intersecting.

list1: 3,1,5,9
                7,2,1   7 is intersection node
list2:  ,2,4,6

Testing. Create list3 7,2,1
Add method to LinkedList to join the list at the end.
Create list1 and list2
Join list1 to list3
Join list2 to list3
Test intersection
Implement intersection function

"""
from linked_list import LinkedList

def intersection(l1, l2):
    if (l1.head or l2.head) is None:
        return None
    else:
        len1 = len(l1)
        len2 = len(l2)
        l1,l2 = (l1,l2) if len1 >= len2 else (l2,l1)
        offset = len1 - len2
        n1 = l1.head
        for i in range(offset):
            n1 = n1.next
        n2 = l2.head
        while n1:
            if n1 is n2:
                return n1
            else:
                n1 = n1.next
                n2 = n2.next
        return None
            


def test_intersect_empty_list():
    l1 = LinkedList()
    l2 = LinkedList()
    intersect = intersection(l1, l2)
    assert intersect is None
    print("test_intersect_empty_list PASS")

def test_intersect_diff_lists():
    l1 = LinkedList([3,1,5,9])
    l2 = LinkedList([2,4,6])
    intersect = intersection(l1, l2)
    assert intersect is None
    print("test_intersect_diff_lists PASS")

def test_intersection():
    l1 = LinkedList([3,1,5,9])
    l2 = LinkedList([2,4,6])
    l3 = LinkedList([7,2,1])
    l1l3 = l1.join(l3)
    #print(l1l3)
    l2l3 = l2.join(l3)
    #print(l2l3)
    intersect = intersection(l1l3, l2l3)
    #print(f"intersect: {intersect.value}")
    assert intersect is l3.head
    print("test_intersection PASS")


test_intersect_empty_list()
test_intersect_diff_lists()
test_intersection()

