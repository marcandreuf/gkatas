def power(base, exp):
    assert base >= 0 and int(base) == base and exp >= 0 and int(exp) == exp, 'Base and exp must be a positive and integer number'
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)


def testPower():
    assert 1 == power(0, 0)
    assert 0 == power(0, 1)
    assert 0 == power(0, 2)
    assert 1 == power(1, 0)
    assert 1 == power(1, 2)
    assert 1 == power(1, 3)
    assert 1 == power(2, 0)
    assert 2 == power(2, 1)
    assert 3 == power(3, 1)
    assert 9 == power(3, 2)
    assert 16 == power(4, 2)
    assert 343 == power(7, 3)
    print('testPower Pass')

testPower()

