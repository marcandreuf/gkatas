def gcd(a,b):
    assert int(a) ==a and int(b) == b, 'A and B must be integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def test_gcd():
    assert 1 == gcd(1, 0)
    assert 4 == gcd(8, 12)
    assert 6 == gcd(48, 18)
    assert 6 == gcd(48, -18)
    print('test_gcd Pass')

def test_FloatNum():
    try:
        gcd(48, 1.8)
    except:
        print('test_FloatNum Pass')


test_gcd()
test_FloatNum()


