"""
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

list1 = 7->1->6
list2 = 5->9->2

add 617+295=912

sumList = 2->1->9

"""
from linked_list import LinkedList, Node

def sum_list(l1, l2):
    if l1.head == None:
        return l2
    elif l2.head == None:
        return l1
    else:
        l3 = LinkedList()
        len1 = len(l1)
        len2 = len(l2)
        l1, l2 = (l1,l2) if len1>=len2 else (l2,l1)
        n1 = l1.head
        n2 = l2.head
        carry = 0
        while n1:
            digits_sum = n1.value + n2.value
            if digits_sum >= 10:
                digits_sum = digits_sum % 10
                l3.add(digits_sum+carry)
                carry = 1
            else:
                l3.add(digits_sum+carry)
                carry = 0
            n1 = n1.next
            n2 = n2.next if n2.next else Node(0)            
        return l3

def test_sum_empty_lists():
    list_1 = LinkedList([])
    list_2 = LinkedList([])
    result_list = sum_list(list_1, list_2)
    assert f"{result_list}" == "[]"
    print("test_sum_empty_list PASS")


def test_sum_empty_list1():
    list_1 = LinkedList([])
    list_2 = LinkedList([1])
    result_list = sum_list(list_1, list_2)
    assert f"{result_list}" == "[1]"
    
    list_1 = LinkedList([1])
    list_2 = LinkedList([])
    result_list = sum_list(list_1, list_2)
    assert f"{result_list}" == "[1]"
    print("test_sum_empty_list1 PASS")

def test_sum_lists():
    list_1 = LinkedList([7,1,6])
    list_2 = LinkedList([5,9,2])
    result_list = sum_list(list_1, list_2)
    assert f"{result_list}" == "[2 -> 1 -> 9]"
    print("test_sum_lists PASS")


def test_sum_lists_dif_sizes():
    list_1 = LinkedList([7,1])
    list_2 = LinkedList([5,9,2])
    result_list = sum_list(list_1, list_2)
    #print(result_list)
    assert f"{result_list}" == "[2 -> 1 -> 3]"

    list_1 = LinkedList([7,1,6])
    list_2 = LinkedList([5,9])
    result_list = sum_list(list_1, list_2)
    #print(result_list)
    assert f"{result_list}" == "[2 -> 1 -> 7]"    

    print("test_sum_lists_dif_sizes PASS")

test_sum_empty_lists()
test_sum_empty_list1()
test_sum_lists()
test_sum_lists_dif_sizes()

