def poa(a):
	assert len(a) > 0, 'Array must not be empty'
	if len(a) == 1:
		return a[0]
	else:
		return a[0] * poa(a[1:])	
	
def test_product_of_array():
	assert 10 == poa([10])
	assert 1 == poa([1])
	assert 2 == poa([1,2])
	assert 6 == poa([1,2,3])
	assert 60 == poa([1,2,3,10])	
	print('product_of_array Pass')
	
def test_empty_array():
	try:
		poa([])
		print('test_empty_array Fail')
	except AssertionError as ae:
		assert 'not be empty' in f'{ae}'
		print('test_empty_array Pass')
		
	
test_product_of_array()
test_empty_array()

