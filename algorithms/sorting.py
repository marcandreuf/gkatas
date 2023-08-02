import math


def buble_sort(list):
    count = 0
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                _swap(list, j, j+1)
                count = count + 1
    # print(f"buble_sort count {count}")


def buble_sort_optim(list):
    count = 0
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                _swap(list, i, i+1)
                count = count + 1
                ordered = False
    # print(f"buble_sort_optim count {count}")


def _swap(list, e1, e2):
    list[e1], list[e2] = list[e2], list[e1]


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


def selection_sort(list):
    for s in range(len(list)):
        #print(f"step: {s}")
        m = s
        for i in range(s+1, len(list)):
            if list[i] < list[m]:
                m = i
        _swap(list, s, m)

def test_selection_sort():
    l = [3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    selection_sort(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_selection_sort PASS")


def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

def test_insertion_sort():
    l = [3, 5, 2, 7, 9, 3, 4, 6, 7, 5]
    insertion_sort(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_insertion_sort PASS")


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


def merge_sort(list):
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        half = len(list) // 2 
        _left = list[:half]
        _right = list[half:]
        return _merge(merge_sort(_left), merge_sort(_right))
    
def _merge(list_a, list_b):
    ret = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            ret.append(list_a[i])
            i += 1
        else:
            ret.append(list_b[j])
            j += 1

    while i < len(list_a):
        ret.append(list_a[i])
        i += 1

    while j < len(list_b):
        ret.append(list_b[j])
        j += 1  

    return ret


def test_merge():
    assert _merge([1], []) == [1]
    assert _merge([], [1]) == [1]
    assert _merge([1], [2]) == [1,2]
    assert _merge([1,3], [2]) == [1,2,3]
    assert _merge([1,3], [2,4,5]) == [1,2,3,4,5]
    assert _merge([1,3], [2,4,5,6]) == [1,2,3,4,5,6]
    assert _merge([2,3], [4,5]) == [2,3,4,5]
    assert _merge([2,3,4,7], [5,6,7,9]) == [2,3,4,5,6,7,7,9]
    print("test_merge PASS")    


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1,2]) == [1,2]
    assert merge_sort([2,1]) == [1,2]
    assert merge_sort([3,5,2,7,9,3,4,6,7,5]) == [2,3,3,4,5,5,6,7,7,9]
    print("test_merge_sort PASS")


   
def quick_sort(list):
    ret = []
    if len(list) <= 1:
        return list
    pivot = _pivot(list)    
    # print(f"piv: {pivot}")
    ret += quick_sort(list[:pivot])
    ret.append(list[pivot])        
    ret += quick_sort(list[pivot+1:])
    # print(f"ret: {ret}")
    return ret

def _pivot(list):
    piv = swap = 0
    if len(list) > 0:
        for i in range(1, len(list)):
            if(list[i] < list[piv]):
                swap += 1
                _swap(list, i, swap)
        _swap(list, piv, swap)
    return swap


def test_pivot():
    assert _pivot([]) == 0
    assert _pivot([1]) == 0
    assert _pivot([1,2]) == 0
    assert _pivot([2,1]) == 1
    assert _pivot([2,1,3]) == 1
    assert _pivot([3,2,1]) == 2
    assert _pivot([3,5,0,6,2,1,4]) == 3


def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([1]) == [1]
    assert quick_sort([2,1]) == [1,2]
    assert quick_sort([3,5,2,7,9,3,4,6,7,5]) == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_quick_sort PASS")



def heap_sort(list):
    pass

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
test_merge()
test_merge_sort()
test_pivot()
test_quick_sort()
test_heap_sort()
