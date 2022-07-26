def rv(word):
	if len(word) <= 1:
		return word
	else:
		pivot = len(word)//2		
		return rv(word[pivot:]) + rv(word[:pivot]) 
	
	
def test_reverse():
	assert '' == rv('')
	assert 'a' == rv('a')
	assert 'ba' == rv('ab')
	assert 'cba' == rv('abc')
	assert 'dcba' == rv('abcd')
	assert 'nohtyp' == rv('python')
	assert 'appmillers' == rv('srellimppa')
	print('test_reverse Pass')
	
test_reverse()

