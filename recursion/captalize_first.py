def capitalizeFirst(arr):
	resutl_arr = []
	if len(arr) <= 0:
		return arr
	item = arr[0]
	resutl_arr.append(f'{item[:1].upper()}{item[1:]}')
	resutl_arr.extend(capitalizeFirst(arr[1:]))
	return resutl_arr


def test_capitalizeFirst():
	assert capitalizeFirst([]) == []
	assert capitalizeFirst(['a']) == ['A']
	assert capitalizeFirst(['car']) == ['Car']
	assert capitalizeFirst(['car', 'taco']) == ['Car', 'Taco']
	assert capitalizeFirst(['car', 'taco', 'banana']) == ['Car','Taco','Banana']
	print('test_capitalizeFirst Pass')


test_capitalizeFirst()
