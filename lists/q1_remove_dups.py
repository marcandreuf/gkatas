from linked_list import LinkedList


def remove_dups(lst):
    node = lst.head
    uniq_set = set()
    # do while loop
    while True:
        if node is None:
            break
        uniq_set.add(node.value)
        if node.next is not None: 
            if node.next.value in uniq_set:
                print(f"remove: {node.next.value}")
                node.next = node.next.next
            node = node.next
        elif node.value in uniq_set:
            node = None
    return lst

# While loop
#        uniq_set = set([node.value])
#        while node:
#            if node.next.value in uniq_set:
#                node.next = node.next.next
#            else:
#                uniq_set.add(node.value)
#                node = node.next
#        return lst
#

def remove_dups_in_place(lst):
    if lst.head == None:
        return
    node = ll.head
    while node:
        r = node
        while r.next:
            if r.next.value == node.value:
                print(f"remove {r.next.value} eq to {node.value}")
                r.next = r.next.next
            else:
                r = r.next
        node = node.next
    return lst


ll = LinkedList()
print(remove_dups(ll))
for i in range(10):
    ll.generate(10,0,99)
    print(f"---- iter {i} ----")
    print(ll)
    print(remove_dups(ll))

print("------- Run in place ----------")
for i in range(10):
    print(f"---- iter in place {i} ----")    
    ll.generate(10,0,99)
    print(ll)
    print(remove_dups_in_place(ll))


