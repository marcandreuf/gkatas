def sumDigits(n):
    assert n >= 0 and int(n) == n, 'Must be a positive integer number'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumDigits(int(n//10))




def testSumDigits():
    assert 0 == sumDigits(0)
    assert 1 == sumDigits(1)
    assert 9 == sumDigits(54)
    print('testSumDigits Pass')


def testNegativeNum():
    try:
        sumDigits(-11)
    except AssertionError as ae:
        assert 'positive' in f'{ae}'
        print('testNegativeNum Pass')

def testFloatNum():
    try:
        sumDigits(1.5)
    except AssertionError as ae:
        assert 'integer' in f'{ae}'
        print('testFloatNum Pass')

testSumDigits()
testNegativeNum()
testFloatNum()
