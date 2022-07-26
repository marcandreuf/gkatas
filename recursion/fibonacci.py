def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Must be positive and integer number'
    if( n in [0,1]):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)




def testFibonacci():
    assert 0 == fibonacci(0), 'f(0) is 0'
    assert 1 == fibonacci(1), 'f(1) is 1'
    assert 1 == fibonacci(2), 'f(2) is 1'
    assert 2 == fibonacci(3), 'f(3) is 2'
    assert 3 == fibonacci(4), 'f(4) is 3'
    assert 5 == fibonacci(5), 'f(5) is 5'
    assert 8 == fibonacci(6), 'f(6) is 8'
    assert 13 == fibonacci(7), 'f(7) is 13'
    print('testFibonacci Pass')


def testNegativeNum():
    try:
        fibonacci(-1)
    except AssertionError as ae:
        assert 'positive' in f'{ae}'
        print('testNegativeNum Pass')

def testFloatNum():
    try:
        fibonacci(1.5)
    except AssertionError as ae:
        assert 'integer' in f'{ae}'
        print('testFloatNum Pass')

testFibonacci()
testNegativeNum()
testFloatNum()

