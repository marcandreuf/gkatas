import math


def buble_sort(list):
    count = 0
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                swap(list, j, j+1)
                count = count + 1
    # print(f"buble_sort count {count}")


def buble_sort_optim(list):
    count = 0
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                count = count + 1
                ordered = False
    # print(f"buble_sort_optim count {count}")


def swap(list, e1, e2):
    list[e1], list[e2] = list[e2], list[e1]


def selection_sort(list):
    for s in range(len(list)):
        #print(f"step: {s}")
        m = s
        for i in range(s+1, len(list)):
            if list[i] < list[m]:
                m = i
        swap(list, s, m)


def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


def bucket_sort(list):
    max_value = max(list)    
    num_buckets = _num_of_buckets(list)
    buckets = [[] for i in range(num_buckets)]    
    bucket_index = 0

    for e in list:
        bucket_index = math.ceil((e * num_buckets)/max_value)-1 
        buckets[bucket_index].append(e)

    for i in range(len(buckets)):
        insertion_sort(buckets[i])
    
    result = []
    for b in buckets:
        result += b

    return result

def _sqrt_list_len(list):
    return math.sqrt(len(list))

def _num_of_buckets(list):
    return round(math.sqrt(len(list)))


def merge_sort():
    pass


def quick_sort():
    pass


def test_buble_sort():
    l = [1, 2, 3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    buble_sort(l)
    assert l == [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_buble_sort PASS")


def test_buble_sort_optim():
    l = [1, 2, 3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    buble_sort_optim(l)
    assert l == [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("buble_sort_optim PASS")


def test_selection_sort():
    l = [3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    selection_sort(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_selection_sort PASS")


def test_insertion_sort():
    l = [3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    insertion_sort(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_insertion_sort PASS")



def test_sqrt_list_len():
    assert _sqrt_list_len([]) == 0
    assert _sqrt_list_len([1]) == 1
    assert _sqrt_list_len([1,2]) == 1.4142135623730951
    assert _sqrt_list_len([3, 5, 2, 7, 9, 3, 4, 6, 7, 5]) == 3.1622776601683795
    print("test_sqrt_list_len PASS")

def test_num_of_buckets():
    assert _num_of_buckets([]) == 0
    assert _num_of_buckets([3, 5, 2, 7, 9, 3, 4, 6, 7, 5]) == 3
    assert _num_of_buckets([1,2]) == 1
    assert _num_of_buckets([1,2,3]) == 2
    assert _num_of_buckets([1,2,3,4]) == 2
    assert _num_of_buckets([1,2,3,4,5]) == 2
    assert _num_of_buckets([1,2,3,4,5,6]) == 2
    assert _num_of_buckets([1,2,3,4,5,6,7,8,9]) == 3
    print("test_num_of_buckets PASS")


def test_bucket_sort():
    assert bucket_sort([3, 5, 2, 7, 9, 3, 4, 6, 7, 5]) == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_bucket_sort PASS")




# TODO test_merge_sort
def test_merge_sort():
    #l = [3,5,2,7,9,3,4,6,7,5]
    # merge_sort(l)
    # print(l)
    #assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_merge_sort PENDING")

# TODO test_quick_sort


def test_quick_sort():
    #l = [3,5,2,7,9,3,4,6,7,5]
    # quick_sort(l)
    # print(l)
    #assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_quick_sort PENDING")

# TODO test_heap_sort


def test_heap_sort():
    #l = [3,5,2,7,9,3,4,6,7,5]
    # heap_sort(l)
    # print(l)
    #assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_heap_sort PENDING")


test_buble_sort()
test_buble_sort_optim()
test_selection_sort()
test_insertion_sort()
test_sqrt_list_len()
test_num_of_buckets()
test_bucket_sort()
# test_merge_sort()
# test_quick_sort()
# test_heap_sort()
