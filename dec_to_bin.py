def d2b(n):
    assert int(n) == n, 'n must be an integer number'
    if n == 0:
        return 0
    else:
        return n%2 + 10*d2b(int(n/2))

def test_d2b():
    assert 0 == d2b(0)
    assert 1 == d2b(1)
    assert 10 == d2b(2), f'{d2b(2)} should be 10'
    assert 11 == d2b(3), f'{d2b(3)} should be 11'
    assert 1101 == d2b(13), f'{d2b(13)} should be 1101'
    assert 1010 == d2b(10), f'{d2b(10)} should be 1010'
    assert 1101 == d2b(-13), f'{d2b(-13)} should be 1101'
    print('test_d2b Pass')


def test_floatNum():
    try:
        d2b(1.2)
        print('test_floatNum Fail')
    except AssertionError as ae:
        assert 'integer' in f'{ae}'
        print('test_floatNum Pass')


test_d2b()
test_floatNum()


