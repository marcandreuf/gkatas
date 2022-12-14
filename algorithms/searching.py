import math

def linear_search(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

def binary_search(lst, value):
    s = 0
    e = len(lst)-1
    m = -1
    while s<e:
        m = math.floor((s+e)/2)
        #print(f's: {s}, e: {e}, m: {m}')
        if value < lst[m]:
            e = m-1
        else:
            s = m+1
    return m

def _sample_list():
    return [8,9,12,15,17,19,20,21,28]

def test_linear_search():
    l = _sample_list()
    print(l)
    assert linear_search(l, -1) == -1, '-1 does not exists in the list'
    assert linear_search(l, 15) == 3, '15 exists in the list'
    assert linear_search(l, 30) == -1, '30 does not exists in the list'
    print('test_linear_search PASS')
    

def test_binary_search():
    l = _sample_list()
    print(l)
    assert linear_search(l, -1) == -1, '-1 does not exists in the list'
    assert binary_search(l, 15), '15 exists in the list'
    assert binary_search(l, 30), '30 does not exists in the list'
    print('test_binary_search PASS')


test_linear_search()
test_binary_search()

