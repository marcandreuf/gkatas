myList = [1, 2, 3, 4]

def middle(lst):
    tml = lst[1:]
    return tml[:-1]

assert middle(myList) == [2,3]
print('test middle Pass')


myList2D= [[1,2,3],[4,5,6],[7,8,9]]

def sumDiagonal(a):
    result = 0
    for i in range(len(a)):
        result += a[i][i]
    return result

assert sumDiagonal(myList2D) == 15
print('test sumDiagonal Pass')



myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def firstSecond(givenList):
    st = 0
    nd = 0
    for i in range(len(givenList)):
        if givenList[i] >= st:
            nd = st
            st = givenList[i]
    return st, nd


firstSecond(myList) == 90, 87
print('test firstSecond Pass')



def missingNumber(myList, totalCount):
	totalResult = totalCount*(totalCount+1) / 2
	totalList = 0
	for i in range(len(myList)):
		totalList += myList[i]
	return totalResult - totalList 
	
assert missingNumber([1, 2, 3, 4, 6], 6) == 5
print('test missingNumber Pass')


myList = [1, 1, 2, 2, 3, 4, 5]

def removeDuplicates(myList):
    newList = []
    for i in range(len(myList)):
        if len(newList) == 0 or myList[i] != newList[-1]:
            newList.append(myList[i])
    return newList

assert removeDuplicates(myList) == [1,2,3,4,5]
print('test removeDuplicates Pass')


pairsList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]

def pairSum(lst, target):
    r = []
    c = []
    for i in range(len(lst)):
        if lst[i] in c:
            r.append(f'{target-lst[i]}+{lst[i]}')        
        c.append(target-lst[i])
    return r

assert pairSum(pairsList, 7) == ['4+3', '2+5', '3+4', '-2+9']
print('test pairSum Pass')









