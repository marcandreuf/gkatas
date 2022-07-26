def fib(n):
	if n in [0,1]:
		return n
	else:
		return fib(n-1) + fib(n-2)
	

def test_fib():
	assert 0 == fib(0)
	assert 1 == fib(1)
	assert 1 == fib(2)
	assert 2 == fib(3)
	assert 3 == fib(4)
	assert 55 == fib(10)
	assert 317811 == fib(28)
	assert 9227465 == fib(35)
	print('test_fib Pass')
	
test_fib()
