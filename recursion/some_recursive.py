def some_recursive(arr, cb):
	if len(arr) == 1:
		#print(f'last one {arr[0]}, {cb(arr[0])}')
		return cb(arr[0])
	else:
		#print(f'{arr[0]}, {cb(arr[0])}')
		return cb(arr[0]) or some_recursive(arr[1:], cb)


def isOdd(num):
	return False if num%2==0 else True


def test_some_recursive():
	assert some_recursive([1,2,3,4], isOdd), 'expected to be True'
	assert some_recursive([4,6,8,9], isOdd), 'expected to be True'
	assert some_recursive([4,6,8], isOdd) == False, 'expected to be False'
	print('test_some_recursive Pass')

test_some_recursive()
