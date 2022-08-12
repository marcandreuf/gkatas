def capitalize_words(arr):
	if len(arr) == 0:
		return []

	result = []
	result.append(arr[0].upper())
	result.extend(capitalize_words(arr[1:]))
	return result

words = ['i', 'am', 'learning', 'recursion']

def test_capitalize_words():
	assert capitalize_words([]) == []	
	assert capitalize_words(['a']) == ['A']
	assert capitalize_words(['a', 'b']) == ['A', 'B']
	assert capitalize_words(words) == \
		['I', 'AM', 'LEARNING', 'RECURSION']
	print('test_capitalize_words Pass')

test_capitalize_words()