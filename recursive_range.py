def rr(n):
	if n == 0:
		return 0
	else:
		return n + rr(n-1)
	
	
def test_recursive_range():
	assert 0 == rr(0)
	assert 1 == rr(1)
	assert 3 == rr(2)
	assert 21 == rr(6)
	assert 55 == rr(10)
	print('test_recursive_range Pass')
	
test_recursive_range()
