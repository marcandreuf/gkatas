from array import array

def rv(word):
	if len(word) < 2:
		return word 

	ar = array('u')
	ar.fromunicode(word)
	i = 0
	e = len(ar)-1
	while(i < e):
		#print(f'swap {i} {ar[i]} and {e} {ar[e]}')
		temp = ar[i]
		ar[i] = ar[e]
		ar[e] = temp
		i += 1
		e -= 1
	#print(f'result {ar.tounicode()}')
	return ar.tounicode()

	
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