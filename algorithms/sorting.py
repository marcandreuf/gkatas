

def buble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


def selection_sort(list):
    for s in range(len(list)):
        #print(f"step: {s}")
        m = s
        for i in range(s+1,len(list)):
            if list[i] < list[m]:
                m = i
        list[s], list[m] = list[m], list[s]
        #print(list)

def test_buble_sort():
    l = [3,5,2,7,9,3,4,6,7,5]
    buble_sort(l)
    print(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_buble_sort PASS")


def test_selection_sort():
    l = [3,5,2,7,9,3,4,6,7,5]
    selection_sort(l)
    print(l)
    assert l == [2, 3, 3, 4, 5, 5, 6, 7, 7, 9]
    print("test_selection_sort PASS")

test_buble_sort()
test_selection_sort()



