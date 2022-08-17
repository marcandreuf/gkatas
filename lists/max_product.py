myArray = [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]


def find_max_prod(arr):	
	max_1 = 0
	max_2 = 0
	if len(arr) == 0:
		return (0,0,0)
	else:
		for i in range(len(arr)):
			if arr[i] > max_1:
				max_2 = max_1
				max_1 = arr[i]			
	return (max_2, max_1, max_1 * max_2)


def test_find_max_prod():
	assert find_max_prod([]) == (0,0,0)
	assert find_max_prod([1]) == (0,1,0)
	assert find_max_prod([1, 2]) == (1,2,2)
	print(f'prod {find_max_prod(myArray)}')
	assert find_max_prod(myArray) == (57,58,(57*58))
	print('test_find_max_prod Pass')

test_find_max_prod()

