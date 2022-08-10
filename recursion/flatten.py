def flatten(arr):
	#print(f'flatten {arr}')
	resutl_arr = []
	for item in arr:
		if isinstance(item, list):
			#print(f'flatten inner array {item}')
			resutl_arr.extend(flatten(item))
		else:
			#print(f'append item {item}')
			resutl_arr.append(item)
	return resutl_arr


def test_flatten():
	assert flatten([]) == []
	assert flatten([1]) == [1]
	assert flatten([1, 2, 3, [4, 5]]) == [1, 2, 3, 4, 5]
	assert flatten([1, [2, [3, 4], [[5]]]]) == [1, 2, 3, 4, 5]
	assert flatten([[1], [2], [3]]) == [1, 2, 3]
	assert flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) == [1, 2, 3]
	print(f'test_flatten Pass')

test_flatten()
