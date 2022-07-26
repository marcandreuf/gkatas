
def factorial(n):
    assert n >= 0 and int(n) == n, 'Must be a positive number and integer only'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


def test_factorial():
    assert 1 == factorial(0)
    assert 24 == factorial(4), "should be 24"
    print('test_factorial Pass')

def test_negativeNumber():
    try:
        factorial(-1)
    except AssertionError as aerror:
        assert 'Must be a positive' in f'{aerror}'
        print('test_negativeNumber Pass')

def test_nonIntegerNumber():
    try:
        factorial(-0.5)
    except AssertionError as aerror:
        assert 'and integer only' in f'{aerror}'
        print('test_nonIntegerNumber Pass')


test_factorial()
test_negativeNumber()
test_nonIntegerNumber()


